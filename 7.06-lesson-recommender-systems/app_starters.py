from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, world!"

@app.route('/idk')
def blahblahblah():
    return "blah blah blah"

