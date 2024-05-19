from django.urls import path
from . import views

urlpatterns = [
  path('<str:nickname>/', views.user_detail),
]