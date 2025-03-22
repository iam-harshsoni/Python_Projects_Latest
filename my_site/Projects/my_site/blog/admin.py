from django.contrib import admin
from .models import Author,Tag,Post
# Register your models here.


admin.site.register(Author)
admin.site.register(Tag)


class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date",)
    list_display = ("title", "date", "author",)

admin.site.register(Post,PostAdmin)