from django import forms
from django.forms import ModelForm, fields
from .models import Contact


# Contact form
class ContactForm(ModelForm):
  class Meta:
    model = Contact
    fields =  '__all__'

  def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
          field.widget.attrs['class'] = 'form-control'
