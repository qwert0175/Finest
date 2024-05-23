from django.urls import path
from . import views

urlpatterns = [
    path('', views.getProductsInfo),
    path('deposit/', views.getDeposits),
    path('deposit/<str:fin_cd>/', views.getDepositOne),
    path('saving/', views.getSavings),
    path('saving/<str:fin_cd>/', views.getSavingOne),
    path('creditloan/', views.getCreditLoans),
]
