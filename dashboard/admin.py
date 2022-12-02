from django.contrib import admin
from .models import CountryData

# Register your models here.
list_display = ('country', 'population')

admin.site.register(CountryData)
