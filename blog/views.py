from turtle import pos
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.test import tag
from blog.models import Post, Comment
from blog.forms import CommentForm
from taggit.models import Tag
from django.db.models import Count

# Create your views here.


def post_list(request, tag_slug=None):
    # Retrieves a list of all published posts
    posts = Post.published.all()
    # Get the latest post from the list of posts
    featured_post = posts.earliest()
    # Create a new list of posts excluding the latest post
    # This new list becomes the one to be rendered in the template
    posts_list = posts.exclude(publish__exact=featured_post.publish)

    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts_list = posts_list.filter(tags__in=[tag])

    paginator = Paginator(posts_list, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver always the first page
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/list.html', {
            'posts': posts,
            'page': page,
            'featured_post': featured_post,
            'tag': tag,
    })


# Retrieve details of a single post
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    # List of actives comments for each posts
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        # Comment posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create the comment but don't save it yet
            new_comment = comment_form.save(commit=False)
            # Assign the post to the comment
            new_comment.post = post
            # Save the comment 
            new_comment.save()
    else:
        comment_form = CommentForm()

        return render(request, 'blog/post/detail.html', {
            'post': post,
            'comments': comments,
            'new_comment': new_comment,
            'comment_form': CommentForm()
        })
    return render(request, 'blog/post/detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': CommentForm()
    })


