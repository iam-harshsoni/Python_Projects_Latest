from django.http import Http404
from django.shortcuts import get_object_or_404, render
from datetime import date
from .seed import *
from .models import *


#helper function to get the date
def get_date(post):
    try:
        return post.date
    except Exception as e:
        raise Http404()

# Create your views here.

def index(request):
    try:
        # we can use Django inbuild functions to sort the data by date in descending order
        # we will then slice using [:3] instead of [-3:] as we are already sorting in descending order
        
        """ Note: IMP
            - you might be thinking that this below code will affect the performance as we are 
              getting all the records from the table first and then we are using python to slice
              the data. BUT in django thats not the case, Django will convert this entire code in
              the single SQL query and it will get the top 3 sliced records only.
        """
        all_posts = Post.objects.all().order_by("-date")[:3]

        # sorted_post = sorted(all_posts, key=get_date)
        
        # latest_post = sorted_post[-3:]
        
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