from django.http import Http404
from django.shortcuts import get_object_or_404, render
from datetime import date
from .seed import *
from .models import *

# Create your views here.

def index(request):
    try:
        all_posts = Post.objects.all().order_by("-date")[:3]     
        return render(request, "blog/index.html", {"posts": all_posts})
    
    except Exception as e:
        print(e)
        raise Http404()
        

def posts(request):
    try:
        all_posts = Post.objects.all()
        return render(request, "blog/all-posts.html", {"all_posts" : all_posts})
    except Exception as e:
        raise Http404()

def post_detail(request, slug):
    try:
        request_data = get_object_or_404(Post, slug=slug)
        return render(request, "blog/post-detail.html", {"post": request_data})
    except Exception as e:
        print(e)
        raise Http404()