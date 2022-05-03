from django.contrib import sitemaps
from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
# from portfolio.views import IndexView

# app_name  = 'portfolio'

urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('aboutme/', views.AboutView.as_view(), name='aboutme'),
  # path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
