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
  
  """def form_valid(self, form):
        form.send_email(
            name,
            subject,
            msg,
            ['kingcogles@gmail.com'],
            fail_silently=False,
        )
  """      

  def form_valid(self, form):
        message = "{name} / {email} said: ".format(
            name=form.cleaned_data.get('name'),
            email=form.cleaned_data.get('email'))
        message += "\n\n{0}".format(form.cleaned_data.get('msg'))
    
        send_mail(
            subject=form.cleaned_data.get('subject').strip(),
            msg=message,
            from_email='contact-form@myapp.com',
            recipient_list=[settings.RECIPIENTS_ADDRESS],
        )