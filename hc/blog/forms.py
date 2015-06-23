from django import forms
from django.forms import ModelForm
from blog.models import Post
from markitup.widgets import MarkItUpWidget

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        content = forms.CharField(widget=MarkItUpWidget())