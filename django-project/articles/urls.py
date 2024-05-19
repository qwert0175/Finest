from django.urls import path
from articles import views

urlpatterns = [
    path('', views.article_list),
    path('<int:article_pk>/', views.article_detail),
    path('<int:article_pk>/comment_create/', views.comment_create),
    path('<int:article_pk>/comment_detail/<int:comment_pk>/', views.comment_detail),
    path('<int:article_pk>/likes/', views.likes),
]