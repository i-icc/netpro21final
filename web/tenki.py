import requests
from data import DataSet


def get_w(code):
    url_items = 'https://weather.tsukumijima.net/api/forecast'
    item_data = {
        'city': code
    }
    r = requests.get(url_items, json=item_data)
    return r.json()


def processing_json(r):
    result = {}
    result["locate"] = r["location"]["prefecture"] + r["location"]["city"]
    today = r["forecasts"][0]
    result["weather"] = today["telop"]
    result["wave"] = today["detail"]["wave"]
    result["temp"] = today["temperature"]["max"]["celsius"]
    result["moi"] = today["temperature"]["max"]["fahrenheit"]
    result["降水確率"] = today["chanceOfRain"]
    result["image_svg"] = today["image"]["url"]
    return result


def choice_close():
    pass


def main():
    code = DataSet.city["稚内"]
    print(get_w(code))


if __name__ == "__main__":
    main()
