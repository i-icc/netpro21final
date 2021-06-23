from flask import Flask,render_template,request
from data import DataSet
from tenki import get_w

app = Flask(__name__)

@app.route('/')
def hello():
    data = DataSet
    return render_template('index.html',data=data)

@app.route('/result', methods=['GET'])
def result():
    city = request.args.get('city')
    data = DataSet
    if city not in data.city:
        return render_template('error.html')
    j = get_w(data.city[city])
    return render_template('result.html',q=j)

if __name__ == "__main__":
    app.run(debug=True)