from django.contrib.syndication.views import Feed
from blog.models import Post
from django.urls import reverse


class LatestPostFeed(Feed):
    title = "Blog feed"
    link = ""
    description = "Updates on blog posts"
    # description_template = "post/articles.html"

    def items(self):
        return Post.published.all()[:3]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.title



