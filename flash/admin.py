from django.contrib import admin

# Register your models here.

from .models import Author, Post

admin.site.register(Post)
admin.site.register(Author)
