from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "By Code!"

@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/sum/<int:a>/<int:b>')
def sum(a: int, b: int):
    nums_suim = a + b
    return str(nums_suim)
@app.route('/mult/<int:a>/<int:b>')
def mult(a: int , b: int):
    result = float (a * b)
    return str(result)
