from flask import Flask, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def proxy():
    r = requests.get('http://nginxseatalert.duckdns.org', params=request.args)
    return r.text


if __name__ == '__main__':
    app.run()
