from django.urls import path
from community import views

app_name = 'community'
urlpatterns = [
    path('write/', views.WriteFormView.as_view(), name='write'),
    path('list/', views.ArticleListView.as_view(), name='list'),
    path('view_detail/<slug:pk>/', views.ArticleDetailView.as_view(), name='view_detail'),
    path('change/', views.ArticleChangeView.as_view(), name='change_list'),
    path('<int:pk>/update/', views.ArticleUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='delete'),
]