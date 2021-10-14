from flask import Flask
import os

app = Flask(__name__)


@app.route('/', methods=["GET"])
def get_stuff():
    return "Docker is cool"


if (__name__ == "__main__"):
    app.run('0.0.0.0', port=os.environ['PORT'])
