from django import forms
from django.contrib import admin
from blog.models import Post

#admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'slug')
    list_filter = ('status', 'created', 'publish', 'author')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish' 
    ordering = ('status', 'publish')