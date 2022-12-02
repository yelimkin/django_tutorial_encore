from django.contrib import admin
from community import models

# Register your models here.
from .models import Article

# admin 페이지에 Article 데이터 모델 등록
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('제목', {'fields': ['title']}),
        ('내용', {'fields': ['contents']}),
        ('작성자 정보', {'fields': ['name', 'url', 'email']}),
        ('작성자 id', {'fields':['owner'], 'classes':['collapse']}),
    ]
    list_display = ('title', 'url', 'cdate')
    list_filter = ['cdate']
    search_fields = ['title', 'contents']

admin.site.register(models.Article, ArticleAdmin)
