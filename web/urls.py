
from django.urls import path
from . import views

app_name = 'web'
urlpatterns = [
    path('article/', views.ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('article/<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='article_update'),
    path('article/create/', views.ArticleCreateView.as_view(), name='article_create'),
]