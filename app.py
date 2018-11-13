import os, sys, datetime, random, json
from flask import Flask, session, g, request, render_template, redirect, Response
from flask_mongoengine import MongoEngine

import config
from models import DownloadLog

app = Flask(__name__)

app.config.from_object('config.Config')
db = MongoEngine(app)

@app.before_request
def before_request():
    g.last_ip = request.remote_addr
    print('g.last_ip :', g.last_ip)

@app.route('/')
def index_view():
    return render_template('index.html')


@app.route('/downloads')
def downloads_view():
    with open('./downloads.json') as f:
        downloads = json.load(f)
        return render_template('downloads.html', downloads=downloads, DownloadLog=DownloadLog)


@app.route('/api/download/log', methods=['POST'])
def download_log():
    data = request.get_json()
    key = data['key']

    print(".environ['REMOTE_ADDR'] :", request.environ['REMOTE_ADDR'])
    print("request.remote_addr :", request.remote_addr)

    log = DownloadLog(key=key, ip=request.remote_addr)
    log.save()

    return Response('success', status=200)


if __name__ == '__main__':
    base_dir = os.path.abspath(os.path.dirname(__file__) + '/')
    sys.path.append(base_dir)

    app.secret_key = config.Config.SECRET_KEY
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', False)
    app.run(host='0.0.0.0', debug=FLASK_DEBUG, port=8080)
