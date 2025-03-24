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
    
    def is_stored_post(self, request, post_id):
        
        stored_posts = request.session.get("stored_posts") #Getting the value from session
        
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False
            
        return is_saved_for_later
    
    def get(self, request, slug):
        
        post = Post.objects.get(slug=slug)        
        context = self.post_detail_context(CommentForm(), post, request)

        return render(request, "blog/post-detail.html",context) 

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        
        if comment_form.is_valid():
            
            comment = comment_form.save(commit=False)
            comment.post = post  # Here I am setting the value of post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail",args=[slug]))
        
        context = self.post_detail_context(comment_form, post, request)
        return render(request, "blog/post-detail.html",context) 

    def post_detail_context(self, comment_form, post, request):
        context = {
            "post" : post,
            "post_tags" : post.tags.all(),
            "comment_form" : comment_form,
            "comments" : post.comments.all().order_by("-id"),
            "saved_for_later" : self.is_stored_post(request,post.id)
        }
        
        return context
  
class ReadLaterView(View):
    
    
    def get(self, request):
        stored_posts = request.session.get("stored_posts") #Getting the value from session
        
        context = {}
        
        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
            
        else:
            post = Post.objects.filter(id__in = stored_posts)
            context["posts"] = post
            context["has_posts"] = True
        return render(request, "blog/stored-post.html", context)
            
    def post(self, request):
        stored_posts = request.session.get("stored_posts") #Getting the value from session
        
        if stored_posts is None:
            stored_posts = []
        
        post_id = int(request.POST["post_id"])
        
        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
        
        request.session["stored_posts"] = stored_posts #Setting the value in the session
        
        return HttpResponseRedirect("/")