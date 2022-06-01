from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "By Code!"

@app.route('/sum/<int:a>/<int:b>')
def sum(a: int, b: int):
    nums_suim = a + b
    return str(nums_suim)
