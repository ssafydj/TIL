from django.urls import path
from . import views

# 접근: utilites/index
urlpatterns = [
    path('index/', views.index),
    
]
