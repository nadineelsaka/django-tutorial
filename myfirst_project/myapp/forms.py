from django import forms
from .models import Topic, Post


class NewTopicForm(forms.ModelForm):
    # to customize message from another(Post) model :
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'write your comment'}),
                              max_length=4000,
                              help_text='maximum lenght is 4000 characters')

    class Meta:
        model = Topic
        fields = ['subject', 'message']


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message']
