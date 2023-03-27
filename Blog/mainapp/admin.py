from django.contrib import admin
from .models import Tag, Author, Post, Comment, Category

# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Author)
