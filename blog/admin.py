from datetime import date
from django.contrib import admin
from blog.models import Post, Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ['title', 'headimg', 'slug', 'author', 'publish', 'created', 'updated', 'status']
  list_filter = ['status', 'created', 'publish', 'author']
  search_fields = ['title', 'body']
  prepopulated_fields = {'slug':('title',)}
  raw_id_fields = ['author',]
  date_hierarchy  = 'publish'
  ordering  = ['status', 'publish']  

@admin.register(Comment)
class Comment(admin.ModelAdmin):
  list_display = ['name', 'email', 'post', 'created', 'active']
  list_filter = ['active', 'created', 'updated']
  search_fields = ['name', 'email', 'body']
  
