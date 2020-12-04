from wtforms_alchemy import ModelForm
from models import User, Post

class UserForm(ModelForm):
    class Meta:
        model = User 

class PostForm(ModelForm):
    class Meta:
        model = Post
        include = [
            'user_id',
        ]