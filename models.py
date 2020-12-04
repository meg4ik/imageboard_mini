from main import db
from datetime import date

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False,
        index=True
    )
    user = db.relationship(User, foreign_keys=[user_id, ])

    title = db.Column(db.String(140), unique=True, nullable=False)
    content = db.Column(db.String(3000), nullable=False)

    date_created = db.Column(db.Date, default=date.today)
    is_visible = db.Column(db.Integer, default=1, nullable=False)
    
    def to_json(self):
        return {
            "user": self.user,
            "title": self.title,
            "content": self.content,
            "date_created": self.date_created
        }