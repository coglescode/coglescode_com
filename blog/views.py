from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Post, Comment
from blog.forms import CommentForm


# Create your views here.

# Retrieve a list of all posts
# Pagination function retrieves only 4 posts by page
def post_list(request):
    posts = Post.published.all()
    # Get the latest post
    featured_post = posts.earliest()
    posts_list = posts.exclude(publish__exact=featured_post.publish)

    print(posts_list)

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
