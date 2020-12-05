from main import db
from datetime import date

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(45), nullable=False)
    content = db.Column(db.String(1000), nullable=False)
    date = db.Column(db.Date, default=date.today)



class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    Topic_id = db.Column(
        db.Integer,
        db.ForeignKey('topic.id'),
        nullable=False,
        index=True
    )
    topic = db.relationship(Topic, foreign_keys=[Topic_id, ])

    text = db.Column(db.String(100), nullable=False)

    date = db.Column(db.Date, default=date.today)