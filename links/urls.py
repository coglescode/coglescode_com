from django.urls import path
from links import views
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'links'

urlpatterns = [
    path('', views.LinkList.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)
