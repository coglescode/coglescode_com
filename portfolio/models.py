from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.


class UserIntro(models.Model):
    name = models.CharField(max_length=200)
    # name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_names')
    intro_line = models.CharField(max_length=200)
    descr = models.TextField()  # descr: abbreviation of the word description
    avatar = models.ImageField(upload_to='images')
    cert = models.FileField(upload_to='images')  # cert: abbreviation of the word certificate

    def __str__(self):
        return f'{self.name}'


class Project(models.Model):
    title = models.CharField(max_length=200)
    descr = models.TextField(blank=True)
    img = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.title

    """def get_absolute_url(self):
        return reverse ('projects', kwargs={'title':self.title})
    """


class Contact(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    # msg = models.TextField()
    msg = models.CharField(max_length=80)

    def __str__(self):
        return self.name
