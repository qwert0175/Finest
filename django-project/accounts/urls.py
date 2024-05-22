from django.urls import path
from . import views

urlpatterns = [
  path('deposit/', views.user_deposit),
  path('saving/', views.user_saving),
  path('creditloan/', views.user_creditloan),
  path('<str:username>/', views.user_detail),
  path('<str:username>/product/', views.getUserProduct),
  path('<str:username>/check/', views.getUserInfo),
  path('<str:username>/product/recommend/', views.getProductRecommend),
]