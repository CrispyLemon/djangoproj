from django.urls import path
from . import views
app_name = 'dashboard'

url_patterns = [
    path('', views.index, name = 'index'),
    
    ]