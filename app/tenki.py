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


def choice_close():
    pass


def main():
    code = DataSet.city["稚内"]
    print(get_w(code))


if __name__ == "__main__":
    main()
