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
        # Passing different objects from different models in one context
        # Passing listview objects in same template
        context.update({
            'profile': UserIntro.objects.all(),
            'my_projects': Project.objects.all,
            # 'form': ContactFormView(),
        })
        return context
    
    def form_valid(self, form):
        form.send()
        return super().form_valid(form)
    
class Aboutview(TemplateView):
    template_name = "portfolio/aboutme.html"