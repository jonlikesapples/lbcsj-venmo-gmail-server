from flask import Flask
from os import environ;
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello this is the homepage!'


if __name__ == '__main__':
	app.debug = True
	app.run(debug=True, host='0.0.0.0', port=int(environ.get("PORT", 5000)))
