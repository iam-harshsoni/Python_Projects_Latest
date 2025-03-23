from django.http import Http404
from django.shortcuts import get_object_or_404, render
from datetime import date
from .seed import *
from .models import *
from django.views.generic import ListView, DetailView

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
class PostDetailView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()  # This code will get the Tags for the post. 
        return context
    