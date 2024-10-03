from django.contrib import admin
from .models import Tag, Author, Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','date')
    list_filter = ('title','author','date')


admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Post,PostAdmin)