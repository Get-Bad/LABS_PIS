from django.contrib import admin
from .models import Article

@admin.register(Article) # Альтернатива admin.site.register
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_excerpt', 'created_date')