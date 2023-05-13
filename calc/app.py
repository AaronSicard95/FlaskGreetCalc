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