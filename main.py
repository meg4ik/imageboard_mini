from flask import Flask, request, render_template
from simple_settings import settings
from flask_sqlalchemy import SQLAlchemy
from werkzeug.datastructures import MultiDict

app = Flask(__name__, template_folder="templates")
try:
    app.config.update(**settings.as_dict())
except:
    print ("Please configurate your environment!")

db = SQLAlchemy(app)

@app.route("/Topic", methods=["POST","GET"])
def Topic_fu():
    from models import Topic
    from forms import TopicForm
    if request.method == "POST":
        form = TopicForm(request.form)
        if form.validate():
            topicsql = Topic(**form.data)
            db.session.add(topicsql)
            db.session.commit()
            return render_template('_adding_topic_successful.txt', topicsql=topicsql)
        else:
            return "Form is not valid!", 400 
    try:
        quotes = Topic.query.all()
    except Exception as e:
            return str(e)
    else:
        return render_template('_take_topic_template.txt', quotes=quotes)

@app.route("/Topic/<int:Topic_id_to>", methods=["POST","GET"])
def Comment_fu(Topic_id_to):
    from models import Comment
    from forms import CommentForm
    if request.method == "POST":
        new_request = request.form.to_dict()
        new_request["Topic_id"] = Topic_id_to
        a = MultiDict()
        for x in new_request:
            a.add(x, new_request[x])
        form = CommentForm(a)
        if form.validate():
            commentsql = Comment(**form.data)
            db.session.add(commentsql)
            db.session.commit()
            return render_template('_adding_comment_successful.txt', commentsql=commentsql)
        else:
            return "Comment is not valid!", 400 

    topic_select = Topic.query.filter_by(id = int(Topic_id_to)).first()

    comments_select = Comment.query.filter_by(Topic_id = int(Topic_id_to))
    return render_template('_take_comment_template.txt', topic=topic_select, comments = comments_select)
        
if __name__ == "__main__":
    from models import *
    db.create_all()
    app.run()