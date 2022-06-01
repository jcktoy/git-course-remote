from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "By Code!"

@app.route('/sum/<in:a>/<int:b>')
def sum(a: int, b: int):
    return a + b
