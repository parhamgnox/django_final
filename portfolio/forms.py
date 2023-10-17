from django import forms
from .models import *



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['which_portfolio' , 'name', 'email', 'subject', 'message']

class ReplyForm(forms.ModelForm):

    class Meta:
        model = Reply
        fields = ['which_comment', 'name', 'message']