from django.contrib import admin
from .models import Author,Tag,Post, Comment
# Register your models here.


admin.site.register(Author)
admin.site.register(Tag)


class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date",)
    list_display = ("title", "date", "author",)

admin.site.register(Post,PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_filter = ("user_name", "user_email",)
    list_display = ("user_name", "user_email", "post", "text", )
admin.site.register(Comment, CommentAdmin)