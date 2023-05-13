from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def sayHello():
    return f'<html><body><h1>welcome</h1></body></html>'


@app.route('/welcome/home')
def sayHello():
    return f'<html><body><h1>welcome home</h1></body></html>'


@app.route('/welcome/back')
def sayHello():
    return f'<html><body><h1>welcome back</h1></body></html>'