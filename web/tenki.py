import requests
from data import DataSet

def get_w(code):
    url_items = 'https://weather.tsukumijima.net/api/forecast'
    item_data = {
        'city':code
    }
    r = requests.get(url_items, json=item_data)
    return r.json()

def main():
    code = DataSet.city["稚内"]
    print(get_w(code))

if __name__=="__main__":
    main()