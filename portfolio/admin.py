from django.contrib import admin
from .models import UserIntro, Project, Contact

# Register your models here.
@admin.register(UserIntro)
class UserIntroAdmin(admin.ModelAdmin):
  list_display = ['name', 'intro_line', 'descr', 'avatar', 'cert']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
  list_display = ['title', 'descr', 'img']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
  list_display = ['name', 'email', 'subject', 'msg']
