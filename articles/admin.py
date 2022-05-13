from django.contrib import admin
from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'content', 'photo', 'time_create', 'time_update', 'is_published', 'category',)
    list_display_links = ('author', 'title', 'content',)
    search_fields = ('title', 'content',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

admin.site.register(Article, ArticleAdmin)

admin.site.register(Category, CategoryAdmin)