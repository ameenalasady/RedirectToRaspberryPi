from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def proxy():
    r = requests.get('http://nginxseatalert.duckdns.org', params=request.args)
    return r.text


if __name__ == '__main__':
    app.run()
