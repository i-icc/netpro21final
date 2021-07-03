from flask import Flask, render_template, request
from data import DataSet
from tenki import get_w, processing_json, choice_close

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html', data=DataSet)


@app.route('/result', methods=['GET'])
def result():
    city = request.args.get('city')
    if city not in DataSet.city:
        return render_template('error.html')
    day = request.args.get('day')
    day = 0 if day is None else int(day)
    j = get_w(DataSet.city[city])
    j = processing_json(j,day)
    code = choice_close(j["weather"],j["temp"])
    return render_template('result.html', q=j, code=code)


if __name__ == "__main__":
    app.run(debug=True)
