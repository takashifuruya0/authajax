from django.contrib import admin
from guardian.admin import GuardedModelAdmin

# Register your models here.
from web.models import Article, Category, Tag


@admin.register(Article)
class ArticleAdmin(GuardedModelAdmin):
    list_display = ['name', 'created_by', 'is_for_pro', 'category',]


@admin.register(Category)
class Category(GuardedModelAdmin):
    list_display = ['name', ]


@admin.register(Tag)
class Tag(GuardedModelAdmin):
    list_display = ['name', ]