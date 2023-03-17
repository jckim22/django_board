from django.contrib import admin
from .models import Board

# Register your models here.

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['id','title','author','published_date']
    list_display_links = ['id','title']
    list_per_page = 10
