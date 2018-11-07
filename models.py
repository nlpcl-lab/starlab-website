import datetime
from flask_mongoengine import MongoEngine

db = MongoEngine()


class DownloadLog(db.Document):
    key = db.StringField()
    ip = db.StringField()
    created_at = db.DateTimeField(default=datetime.datetime.now)

    meta = {
        'indexes': [
            'seq',
        ]
    }
