from django.http import Http404
from django.shortcuts import get_object_or_404, render
from datetime import date
from .seed import *
from .models import *

# Create your views here.


def index(request):
    """
    View function to render the homepage.

    - Fetches the latest 3 posts, ordered by date (descending).
    - Passes the posts to the 'index.html' template for rendering.
    - If an error occurs, it prints the error and raises a 404 exception.
    """
    try:
        all_posts = Post.objects.all().order_by("-date")[:3]  # Get the latest 3 posts
        return render(request, "blog/index.html", {"posts": all_posts})

    except Exception as e:
        print(e)  # Print the error for debugging
        raise Http404()  # Return a 404 error if something goes wrong


def posts(request):
    """
    View function to display all blog posts.

    - Fetches all posts from the database.
    - Passes them to the 'all-posts.html' template.
    - If an error occurs, raises a 404 exception.
    """
    try:
        all_posts = Post.objects.all()  # Fetch all posts
        return render(request, "blog/all-posts.html", {"all_posts": all_posts})

    except Exception as e:
        raise Http404()  # Return a 404 error if an exception occurs


def post_detail(request, slug):
    """
    View function to display a single blog post.

    - Retrieves a post by its slug from the database.
    - Passes the post to the 'post-detail.html' template.
    - If the post is not found, it raises a 404 error.
    """
    try:
        # Get the post by slug or return 404
        request_data = get_object_or_404(Post, slug=slug)
        return render(request, "blog/post-detail.html", 
                      {"post": request_data,
                       "post_tags" : request_data.tags.all()                       
                       })

    except Exception as e:
        print(e)  # Print error for debugging
        raise Http404()  # Return a 404 error if an exception occurs
