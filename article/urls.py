from django.contrib import admin
from django.urls import path
from . import views

app_name = "article"

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('addarticle/', views.addArticle, name="addarticle"),
    path('remove/<int:id>', views.removeArticle, name="remove"),
    path('article/<int:id>', views.detail, name="detail"),
    path('update/<int:id>', views.updateArticle, name="update"),
    path('', views.articles, name="articles"),
    path('comment/<int:id>', views.addComment, name="comment"),
]