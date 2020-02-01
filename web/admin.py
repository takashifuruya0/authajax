from django.contrib import admin
from guardian.admin import GuardedModelAdmin

# Register your models here.
from web.models import Article


@admin.register(Article)
class ArticleAdmin(GuardedModelAdmin):

    class Meta:
        verbose_name = '記事'
        verbose_name_plural = '記事'