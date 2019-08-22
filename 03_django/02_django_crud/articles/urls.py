from django.urls import path
from . import views
#app 에다 urls.py 만들고
urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
    path('<int:pk>/', views.detail),
    path('<int:pk>/delete/', views.delete),
    path('<int:pk>/edit/', views.edit),
    path('<int:pk>/update/', views.update),
]
