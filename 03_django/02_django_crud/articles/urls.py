from django.urls import path
from . import views
#app 에다 urls.py 만들고

app_name = 'articles'
urlpatterns = [
    path 
    path('', views.index, name='index'),
    path('create/', views.create, name='create'), #new(GET) + create(POST)
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'), # EDIT(GET) + UPDATE(POST)
]
