import os, sys, datetime, random
from flask import Flask, session, g, request, render_template, redirect
from flask_mongoengine import MongoEngine

import config
from models import User

base_dir = os.path.abspath(os.path.dirname(__file__) + '/')
sys.path.append(base_dir)

app = Flask(__name__)

app.config.from_object('config.Config')
db = MongoEngine(app)

app.add_url_rule('/', view_func=views.index_page, methods=['GET'])
# app.add_url_rule('/api/doc/<doc_id>', view_func=views.get_doc, methods=['GET'])

if __name__ == '__main__':
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', False)
    app.run(host='0.0.0.0', debug=FLASK_DEBUG, port=8081)
