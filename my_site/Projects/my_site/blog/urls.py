from django.urls import path
# from blog import views
# instead of blog ( app_name ) we can use '.' as we are in the same folder
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('posts/', views.posts, name="all-posts"),

    # slug:slug this slug: is called Transformer
    # posts/my-first-post
    path('posts/<slug:slug>', views.post_detail, name="post-detail")
]
