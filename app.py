import time
from flask import Flask, render_template, request, jsonify, copy_current_request_context
from controller import Controller


app = Flask(__name__, template_folder='templates')
controller = Controller()


@app.route("/")
def hello():
    return render_template('index.html')


@app.route('/search/', methods=["POST"])
def hello_world():  # put application's code here

    search_text = request.get_json()

    result = controller.get_result(search_text.lower())

    return jsonify({'data': result})


if __name__ == '__main__':
    app.run()
