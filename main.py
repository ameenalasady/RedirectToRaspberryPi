from flask import Flask, request, Response
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET'])
def proxy(path):
    url = 'http://nginxseatalert.duckdns.org/' + path
    params = request.args
    headers = {'X-Forwarded-For': request.remote_addr}
    r = requests.get(url, params=params, headers=headers)
    return Response(r.text, status=r.status_code, content_type=r.headers['content-type'])


if __name__ == '__main__':
    app.run()
