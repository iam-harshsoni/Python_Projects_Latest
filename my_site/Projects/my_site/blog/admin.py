from django.contrib import admin
from .models import Author,Tag,Post
# Register your models here.


admin.site.register(Author)
admin.site.register(Tag)


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "image_name"]

admin.site.register(Post,PostAdmin)