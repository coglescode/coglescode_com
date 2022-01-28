from django.shortcuts import render
from . models import Contact, UserIntro, Project
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import ContactForm
from django.core.mail import send_mail


# Create your views here.

# Create your views here.
class IndexView(FormView):
    template_name = 'portfolio/index.html'
    form_class = ContactForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        # context['profile'] = UserIntro.objects.all()
        # Passing different objects from different models with one context
        # Passing listview objects in same template
        context.update({
            'profile': UserIntro.objects.all(),
            'my_projects': Project.objects.all,
            # 'form': ContactFormView(),
        })
        return context

    """def form_valid(self, form):
        message = "{name} / {email} said: ".format(
            name=form.cleaned_data.get('name'),
            email=form.cleaned_data.get('email'))
        message += "\n\n{0}".format(form.cleaned_data.get('msg'))
        send_mail(
            subject=form.cleaned_data.get('subject').strip(),
            message=message,
            from_email='contact-form@myapp.com',
            recipient_list=[settings.LIST_OF_EMAIL_RECIPIENTS],
        )"""

    def form_valid(self, form):
        form.send_email(
            name,
            subject,
            msg,
            ['kingcogles@gmail.com']
        )
        return super().form_valid(form)


"""class ContactFormView(FormView, View):
  #model = Contact
  form_class = ContactForm
  context_object_name = 'form'
  template_name = 'portfolio/index.html'
  success_url = '/'

  def form_valid(self, form):
      form.save()
      #form.send_email()
      return super().form_valid(form)


class ProjectListView(ListView, TemplateResponseMixin):
  model = Project
  #context_object_name = 'my_projects'
  template_name = 'portfolio/index.html'

  def get_context_data(self, **kwargs):
      context = super(ProjectListView, self).get_context_data(**kwargs)
      context['my_projects'] = Project.objects.all() 
      return context 
"""
