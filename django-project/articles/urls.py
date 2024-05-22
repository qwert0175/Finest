from django.urls import path
from articles import views

urlpatterns = [
    path('', views.article_list),
    path('homeview/', views.home_view),
    path('<int:article_pk>/', views.article_detail),
    path('<int:article_pk>/comments/', views.comments),
    path('<int:article_pk>/comment_detail/<int:comment_pk>/', views.comment_detail),
    path('<int:article_pk>/likes/', views.likes),
]