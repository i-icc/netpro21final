import requests

def main():
    url_items = 'https://weather.tsukumijima.net/api/forecast'
    item_data = {
        'city':400040
    }
    r = requests.get(url_items, json=item_data)
    print(r.json())


if __name__=="__main__":
    main()