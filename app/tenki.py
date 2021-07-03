import requests
from data import DataSet


def get_w(code):
    url_items = 'https://weather.tsukumijima.net/api/forecast'
    item_data = {
        'city': code
    }
    r = requests.get(url_items, json=item_data)
    return r.json()


def processing_json(r,day):
    result = {}
    result["locate"] = r["location"]["prefecture"] + r["location"]["city"]
    the_date = r["forecasts"][day]
    result["day"] = the_date["dateLabel"]
    result["weather"] = the_date["telop"]
    result["wave"] = the_date["detail"]["wave"]
    result["temp"] = the_date["temperature"]["max"]["celsius"]
    result["moi"] = the_date["temperature"]["max"]["fahrenheit"]
    result["降水確率"] = the_date["chanceOfRain"]
    result["image_svg"] = the_date["image"]["url"]
    return result

# コーデ選出 (仮)
def choice_close(w,t):
    code = ""
    code_a = "半袖, 半ズボン"
    code_b = "半袖, 長ズボン"
    code_c = "長袖, 長ズボン"
    code_p_a = ",シャツ"
    code_p_b = ",パーカー"
    code_p_c = ",ダウン"

    wet = DataSet.wether
    print(w,t)
    if t == None: return "errer"
    t = int(t)
    if 25 <= t:
        code += code_a
    elif 20 <= t:
        if w in wet["晴"] or w in wet["曇"]:
            code += code_b
        elif w in wet["雨"]:
            code += code_b + code_p_a
    elif 10 <= t:
        if w in wet["晴"]:
            code += code_c
        elif w in wet["曇"] or w in wet["雨"]:
            code += code_c + code_p_a
    elif 0 <= t:
        code += code_c + code_p_b
    elif -5 <= t:
        if w in wet["晴"] or w in wet["曇"]:
            code += code_c + code_p_c
        else:
            code += code_c + code_p_b + code_p_c
    return code



def main():
    code = DataSet.city["稚内"]
    print(get_w(code))


if __name__ == "__main__":
    main()
