import os, sys, datetime, random
from flask import Flask, session, g, request, render_template, redirect
from flask_mongoengine import MongoEngine

import config
from models import DownloadLog

app = Flask(__name__)

app.config.from_object('config.Config')
db = MongoEngine(app)


@app.route('/')
def index_view():
    return render_template('index.html')


@app.route('/downloads')
def downloads_view():
    return render_template('download.html')


if __name__ == '__main__':
    base_dir = os.path.abspath(os.path.dirname(__file__) + '/')
    sys.path.append(base_dir)

    app.secret_key = config.Config.SECRET_KEY
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', True)
    app.run(host='0.0.0.0', debug=FLASK_DEBUG, port=8080)
