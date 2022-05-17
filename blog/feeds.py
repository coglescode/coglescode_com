import imp
from os import truncate
from django.contrib.syndication.views import Feed
from blog.models import Post
from django.urls import reverse_lazy
from django.template.defaultfilters import truncatewords

class LatestPostFeed(Feed):
    title = "Blog feed"
    link = reverse_lazy('blog:post_list')
    description = "New posts on my blog."
    # description_template = "post/articles.html"

    def items(self):
        return Post.published.all()[:3]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)



