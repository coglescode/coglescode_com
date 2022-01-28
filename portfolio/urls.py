from django.urls import re_path, path
from . import views

from portfolio.views import IndexView

urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  #path('projects/<str:title>', views.ProjectListView.as_view(), name='projects')
  #path('contact/', views.ContactFormView.as_view(), name='contact'),
  
]
