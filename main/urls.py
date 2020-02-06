from django.urls import path
from .views import ArticleView
from main import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('articles/', ArticleView.as_view()), #views.articles, name='articles'),
    path('articles/<int:pk>', ArticleView.as_view())
]
