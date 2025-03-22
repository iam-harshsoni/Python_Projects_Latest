from django.http import Http404
from django.shortcuts import get_object_or_404, render
from datetime import date
from .seed import *
from .models import *


#helper function to get the date
def get_date(post):
    try:
        print(post)
        return post.date
    except Exception as e:
        raise Http404()

# Create your views here.

def index(request):
    try:
        # generate_post(n=10)
        all_posts = Post.objects.all()

        sorted_post = sorted(all_posts, key=get_date)
        
        latest_post = sorted_post[-3:]
        print(latest_post)

        return render(request, "blog/index.html", {"posts": latest_post})
    except Exception as e:
        print(e)
        raise Http404()
        

def posts(request):
    try:
        all_posts = Post.objects.all()
        return render(request, "blog/all-posts.html", {"all_posts" : all_posts})
    except Exception as e:
        print(e)
        raise Http404()

def post_detail(request, slug):
    try:
        # all_posts = Post.objects.all()
        # for post in all_posts:
        #     if post.slug == slug:
        #         request_data = post
                
        # ********** OR *************
        """ More efficient than For loop above as 
            Forloop: ( Disadvantages )
                - Inefficient because it keeps looping even after finding a match.
                - if post is not found, request_data might be undefined, causing issues.
            
            next(): (Advantages ✅)
                - More efficient since it stops searching after finding the first match.
                - Shorter and cleaner code.
        
        """

        # Raises StopIteration error if no match is found (unless a default value is provided).
        # Safer to provide defaul value as 'None' at the end to This prevents errors by returning None if no matching post is found.
        
        # request_data = next((post for post in all_posts if post.slug == slug), None)
        
        request_data = get_object_or_404(Post, slug=slug)

        return render(request, "blog/post-detail.html", {"post": request_data})
    
    except Exception as e:
        print(e)
        raise Http404()