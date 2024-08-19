from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('rating', 'body')

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['rating'].widget.attrs.update({'min': 1, 'max': 10})
        self.fields['body'].widget.attrs.update({'placeholder':
                                                'Enter your comment here...'})
