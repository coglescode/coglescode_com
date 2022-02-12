from django import forms
from django.forms import ModelForm, fields
from .models import Contact
from django.conf import settings 
from django.core.mail import send_mail

# Contact form
class ContactForm(ModelForm): 
      class Meta:
            model = Contact
            fields =  '__all__'

            widgets = {
                  'name':forms.TextInput(attrs={'placeholder': 'Name'}),
                  'email':forms.TextInput(attrs={'placeholder': 'Email'}),
                  'subject':forms.TextInput(attrs={'placeholder': 'Subject'}),
                  'msg':forms.Textarea(attrs={'rows':3, 'placeholder': 'Your message goes here ...'}),
            }

            """
            labels = {
                        # This way you hidde the label of the input field
                        'name': '', 
                        'email': '',
                        'subject': '',
                        'msg': '',
                  }
            """    

      def __init__(self, *args, **kwargs):
            super(ContactForm, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                  field.widget.attrs['class'] = 'form-control shadow-sm'
                  field.label = ''

      

      def get_info(self):
            """
            Method that returns formatted information
            :return: subject, msg
            """
            # Cleaned data
            cl_data = super().clean()

            name = cl_data.get('name').strip()
            from_email = cl_data.get('email')
            subject = cl_data.get('subject')

            msg = f'{name} with email {from_email} said:'
            msg += f'\n"{subject}"\n\n'
            msg += cl_data.get('msg')
            return subject, msg, from_email

      def send(self):
            subject, msg, from_email = self.get_info()
            send_mail(
                  subject=subject,
                  message=msg,
                  from_email=from_email,
                  recipient_list=[settings.RECIPIENT_ADDRESS]
            )
      
      """def form_valid(self, form):
            form.send_email(
                  name,
                  subject,
                  msg,
                  ['kingcogles@gmail.com'],
                  fail_silently=False,
            )      

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
      """ 