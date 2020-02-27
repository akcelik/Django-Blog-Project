from django.contrib import admin
from .models import Article, Comment

# Register your models here.

admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "create_date"]
    list_display_links=["title", "create_date"]
    search_fields = ["title"]
    list_filter=["create_date","author"]
    class Meta:
        model = Article
