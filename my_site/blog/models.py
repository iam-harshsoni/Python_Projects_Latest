from django.db import models
from datetime import date
from django.utils.text import slugify
# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=254)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=20, blank=True)
    
    def __str__(self) -> str:
        return f"{self.caption}"

class Post(models.Model):

    author = models.ForeignKey(
        Author, related_name="posts", on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True)
    image = models.ImageField(upload_to="posts", null=True)
    title = models.CharField(max_length=125)
    excert = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    content = models.CharField(max_length=1500)
   
    slug = models.SlugField(default="", editable=False,
                            null=False, db_index=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self) -> str:
        return f"{self.title}"
    
class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField() 
    text = models.TextField(max_length=400)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    
    def __str__(self) -> str:
        return f"{self.user_name} - {self.user_email}"
