from django.urls import path
from . import views

urlpatterns = [
    path('', views.getProductsInfo),
    path('deposit/', views.getDeposits),
    path('saving/', views.getSavings),
    path('creditloan/', views.getCreditLoans),
]
