from dataclasses import field
from pyexpat import model
from django import forms
from blog.models import Comment

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('name', 'email', 'body')

    widgets = {
                  'name':forms.TextInput(attrs={'placeholder': 'Name'}),
                  'email':forms.TextInput(attrs={'placeholder': 'Email'}),
                  'body':forms.Textarea(attrs={'rows':3, 'placeholder': 'Write your comment here ...'}),
    }


  def __init__(self, *args, **kwargs):
            super(CommentForm, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                  field.widget.attrs['class'] = 'form-control shadow-sm'
                  field.label = ''