from django.urls import path
from . import views
#from portfolio.views import IndexView

#app_name  = 'portfolio'

urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('aboutme/', views.AboutView.as_view(), name='aboutme'),
]
