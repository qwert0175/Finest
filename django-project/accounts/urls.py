from django.urls import path
from . import views

urlpatterns = [
  path('<str:username>/', views.user_detail),
  path('deposit/', views.user_deposit),
]