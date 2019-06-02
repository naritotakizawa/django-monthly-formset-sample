from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.MonthlyList.as_view(), name='monthly_list'),
    path('add/', views.MonthlyAdd.as_view(), name='monthly_add'),
    path('update/<int:pk>/', views.monthly_update, name='monthly_update'),
]