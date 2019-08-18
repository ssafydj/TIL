from django.urls import path
from . import views

urlpatterns = [
    # 원래 url은 아래로 작성해 나간다.
    path('index/', views.index), # url 경로 마지막에 /를 붙이는 습관(or error)
    path('introduce/<name>/<int:age>/', views.introduce),
    path('dinner/', views.dinner),
    path('result/', views.result),#항상 트레일링 컴마 , 를 붙이는 습관
    path('image/', views.image),
    path('hello/<name>', views.hello),
    path('times/<int:num1>/<int:num2>/', views.times),
    path('area/<int:r>/', views.area),
    path('template_language/', views.template_language),
    path('isitgwangbok/', views.isitgwangbok),
    path('isbirth/', views.isbirth),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('art/', views.art),
    path('user_new/', views.user_new),
    path('user_create/', views.user_create),
    path('static_example/', views.static_example),
]
