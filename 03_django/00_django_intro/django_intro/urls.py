"""django_intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


# <str:name> str은 default 이므로 생략가능 (형변환가능)
urlpatterns = [    
    path('utilities/', include('utilities.urls')),
    path('pages/', include('pages.urls')),
    # 최상위 프로젝트 폴더에 하위 폴더를 include해서 각 하위폴더가 직접 url 관리하고
    # 최상위 프로젝트 폴더는 하위 폴더에 처음 접근만을 관리
    # app 이름 + url ex) 127.0.0.1:8000/pages/index/ 로 바뀜
    path('admin/', admin.site.urls),  #항상 트레일링 컴마 , 를 붙이는 습관
]
