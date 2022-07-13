from django.contrib import sitemaps
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Post

"""
class StaticViewSitemap(sitemaps.Sitemap):
    changefreq = "always"
    priority = 0.5

    def items(self):
        # return Post.published.filter(is_draft=False)
        return ['post_list']

    def location(self, item):
        return reverse(item)
"""


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, post):
        return post.updated
