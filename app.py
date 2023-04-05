from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    ip = request.environ['REMOTE_ADDR']
    headers = request.headers
    return {
        'ip': ip,
        'headers': headers
        }
