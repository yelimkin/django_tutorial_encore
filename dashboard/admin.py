from django.contrib import admin
from dashboard import models

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('국가', {'fields': ['country']}),
        ('인구', {'fields': ['population']}),
    ]
    list_display = ('country', 'population')

admin.site.register(models.CountryData, ArticleAdmin)
