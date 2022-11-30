"""django_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from community.views import write
# from community.views import articleList
# from community.views import viewDetail
from community.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('write/', write, name='write'), # route path, view의 함수, data
    # path('list/', articleList, name="list"),
    # path('view_detail/<int:num>', viewDetail, name="view_detail"),
    path('', index, name="index"),
    path('community/', include('community.urls')), # community 하위의 파일 include
    path('dashboard/', include('dashboard.urls')),
]
