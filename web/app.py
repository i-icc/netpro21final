from flask import Flask,render_template
from data import DataSet

app = Flask(__name__)

@app.route('/')
def hello():
    data = DataSet
    return render_template('index.html',data=data)

if __name__ == "__main__":
    app.run(debug=True)