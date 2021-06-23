from flask import Flask, render_template, request
from data import DataSet
from tenki import get_w, processing_json

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html', data=DataSet)


@app.route('/result', methods=['GET'])
def result():
    city = request.args.get('city')
    if city not in DataSet.city:
        return render_template('error.html')
    j = get_w(DataSet.city[city])
    j = processing_json(j)
    return render_template('result.html', q=j)


if __name__ == "__main__":
    app.run(debug=True)
