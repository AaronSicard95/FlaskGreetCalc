from flask import Flask
from flask import request

app = Flask(__name__)

from operations import *

@app.route('/math/<operation>')
def doOp(operation):
    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    match operation:
        case "add":
            answer = add(a,b)
        case "sub":
            answer = sub(a,b)
        case "mult":
            answer = mult(a,b)
        case "div":
            answer = div(a,b)
        case _:
            answer = "invalid operation"

    return f'<html><body><h1>{answer}</h1></body></html>'

@app.route('/add')
def doOpAdd(operation):
    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    answer = add(a,b)

    return f'<html><body><h1>{answer}</h1></body></html>'

@app.route('/sub')
def doOpAdd(operation):
    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    answer = sub(a,b)

    return f'<html><body><h1>{answer}</h1></body></html>'

@app.route('/mult')
def doOpAdd(operation):
    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    answer = mult(a,b)

    return f'<html><body><h1>{answer}</h1></body></html>'

@app.route('/div')
def doOpAdd(operation):
    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    answer = div(a,b)

    return f'<html><body><h1>{answer}</h1></body></html>'