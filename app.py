from flask import Flask, jsonify

app = Flask(__name__)

data = [
    {'id': '1', 'name': 'ssyy', 'age': 15, 'info': 'efsdfds'},
    {'id': '2', 'name': 'stym', 'age': 13, 'info': 'jhgj'},
    {'id': '3', 'name': 'qbyc', 'age': 16, 'info': 'esfsdfds'},
    {'id': '4', 'name': 'sbyx', 'age': 17, 'info': 'gdsgdsffds'},
    {'id': '5', 'name': 'ylwm', 'age': 12, 'info': 'gsfdsfsdfds'},
    {'id': '6', 'name': 'tsm', 'age': 19, 'info': 'sfgesgdsdfds'},
    {'id': '7', 'name': 'mly', 'age': 15, 'info': 'edsfsdfds'},
    {'id': '8', 'name': 'sbyx', 'age': 13, 'info': 'efsdfds'},
]


@app.route('/')
def index():
    return jsonify(data)

