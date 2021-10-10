from flask import Flask, jsonify

app = Flask(__name__)

data = [
    {'id': '1', 'name': 'ssyy', 'age': 15, 'info': 'efgesfgesgdsgdsfdsfsdfds'},
    {'id': '2', 'name': 'stym', 'age': 13, 'info': 'jhgj'},
    {'id': '3', 'name': 'qbyc', 'age': 16, 'info': 'esfsdfds'},
    {'id': '4', 'name': 'sbyx', 'age': 17, 'info': 'efgesfgesgdsgdsffds'},
    {'id': '5', 'name': 'ylwm', 'age': 12, 'info': 'gesgdsgdsfdsfsdfds'},
    {'id': '6', 'name': 'tsm', 'age': 19, 'info': 'efgesfgesgdsfdsfsdfds'},
    {'id': '7', 'name': 'mly', 'age': 15, 'info': 'edsfsdfds'}
]


@app.route('/')
def index():
    return jsonify(data)

