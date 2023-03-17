from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda r: redirect('borame_board:index')),
    path('board/', include('borameboard.urls')),
    path('accounts/', include('accounts.urls')),
]
