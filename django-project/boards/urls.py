from django.urls import path
from boards import views

urlpatterns = [
    path('articles/', views.article_list),
    path('article_detail/<int:article_pk>/', views.article_detail),
    path('comment_create/', views.comment_create),
    path('comment_detail/', views.comment_detail),
]