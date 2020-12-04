from flask import Flask, request, render_template
from simple_settings import settings
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="templates")
try:
    app.config.update(**settings.as_dict())
except:
    print ("Please configurate your environment!")

db = SQLAlchemy(app)

@app.route("/User", methods=["POST","GET"])
def User_fu():
    from models import User
    from forms import UserForm
    if request.method == "POST":
        form = UserForm(request.form)
        if form.validate():
            usersql = User(**form.data)
            db.session.add(usersql)
            db.session.commit()
            return "adding!!!", 200
        else:
            return "Form is not valid!", 400 
    else:
        try:
            quotes = User.query.all()
        except Exception as e:
            return str(e)
        else:
            return render_template('Take_Users_template.txt', quotes=quotes)
            #return {"query":[p.to_json() for p in quotes]}

@app.route("/Post", methods=["POST","GET"])
def Post_fu():
    from models import Post
    from forms import PostForm
    if request.method == "POST":
        form = PostForm(request.form)
        if form.validate():
            postsql = Post(**form.data)
            db.session.add(postsql)
            db.session.commit()
            return "adding!!!", 200
        else:
            return "Form is not valid!", 400 
    else:
        try:
            quotes = Post.query.all()
        except Exception as e:
            return str(e)
        else:
            return {"query":[p.to_json() for p in quotes]}
        
if __name__ == "__main__":
    from models import *
    db.create_all()
    app.run()