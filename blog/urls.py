from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap
from blog.feeds import LatestPostFeed


# from blog.models import Post

app_name = 'blog'

sitemaps = {
    # 'static': StaticViewSitemap,
    'post': PostSitemap,
}

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),

    path('latest/posts/', LatestPostFeed()),

]
