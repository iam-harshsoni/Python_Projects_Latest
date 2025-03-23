from django.urls import path
# from blog import views
# instead of blog ( app_name ) we can use '.' as we are in the same folder
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('posts/', views.PostView.as_view(), name="all-posts"),
    path('posts/<slug:slug>/', views.PostDetailView.as_view(), name="post-detail"),
    path('read-later', views.ReadLaterView.as_view(), name="read-later")
]
