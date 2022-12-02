from django.urls import path
from community import views

app_name = 'community'
urlpatterns = [
    path('write/', views.WriteFormView.as_view(), name='write'),
    path('list/', views.ArticleListView.as_view(), name='list'),
    path('view_detail/<int:num>/', views.ArticleDetailView.as_view(), name='view_detail'),
]