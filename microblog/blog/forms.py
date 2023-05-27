from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # Commentモデルを指定する
        fields = ["name", "email", "body"]