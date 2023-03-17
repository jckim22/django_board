from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'borame_board'

urlpatterns = [
    path('', views.index, name='index'),
    path('regist/', views.regist, name='regist'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'), 
]
