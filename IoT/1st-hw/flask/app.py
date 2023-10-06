import flask import Flask, rennder_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return rennder_template('home.html')