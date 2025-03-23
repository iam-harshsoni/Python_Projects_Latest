from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from datetime import date
from django.views.generic import ListView
from django.views import View

from .seed import *
from .models import *
from .forms import *

# Create your views here.

class IndexView(ListView):
    model = Post 
    template_name = "blog/index.html" 
    ordering = ["-date"]
    context_object_name = "posts"
    
    def get_queryset(self):
        base_query =  super().get_queryset()
        data = base_query[:3]
        return data


class PostView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

# No need to pass on any query that look for SLUG. As View inherited from DetailView will automatically look for PK or SLUG and match
# the argument with that.
class PostDetailView(View):

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post" : post,
            "post_tags" : post.tags.all(),
            "comment_form" : CommentForm()
        }
        return render(request, "blog/post-detail.html",context) 

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        
        if comment_form.is_valid():
            
            """
            In Comment-form, I excluded 'post' to be viewed in the form (UI).
            Now when use add the comments, I need to make sure the comment is mapped
            with the correct "Post". To do that I need to link the correct post by
            my own at backend. 
            
            To do that I have to add 'commit=False' this will prevent save() to hit the 
            database and it will instead create a new model instance
            """
            # comment_form.save()
            comment = comment_form.save(commit=False)
            comment.post = post  # Here I am setting the value of post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail",args=[slug]))
        
        
        context = {
            "post" : post,
            "post_tags" : post.tags.all(),
            "comment_form" : comment_form
        }
        return render(request, "blog/post-detail.html",context) 
  