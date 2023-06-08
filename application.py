from flask import Flask

application = Flask(__name__)


@application.route('/')
def hello_world():
    return 'Hello, World! Welcome to TB'


if __name__ == '__main__':
    application.run(debug=True, port=8080)
