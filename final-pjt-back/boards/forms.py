from django import forms
from .models import Board, Comment

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('title', 'content', )
        exclude = ('user', 'like_users',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )