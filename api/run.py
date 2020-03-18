from flask import Flask, request, jsonify
from get_grade import get_grade
import waitress

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def return_grade():
    if request.method == 'GET':
        return "Use POST method please."
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        output = get_grade(username, password)
        return jsonify(output)


if __name__ == '__main__':
    waitress.serve(app, host="127.0.0.1", port=8082)
