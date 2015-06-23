from writingfield.widgets import FullScreenTextarea
from django.forms import ModelForm
from blog.models import Post

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
        'content': FullScreenTextarea()
        }