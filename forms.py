from wtforms_alchemy import ModelForm
from models import Topic, Comment

class TopicForm(ModelForm):
    class Meta:
        model = Topic 

class CommentForm(ModelForm):
    class Meta():
        model = Comment
        include = [
            'Topic_id',
        ]