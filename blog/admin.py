from django.contrib import admin
from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}
    
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', )}
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content']