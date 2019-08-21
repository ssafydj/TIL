<u>post</u> 방식 :get 방식에 없던 <u>form data</u>라는 항목이 있다. 

```
csrf 사이트간 요청 위조 > post 방식의 'hidden 항목'을 없애는 방식으로 홈페이지를 개설하여 사용자 정보를 해킹

{% csrf_token %}

웹 어플리케이션 취약점 중 하나로 사용자가 자신의 의도와 무관하게 공격자가 의도한 행동을 해서 특정 웹페이지의 보안을 무력화 시키거나 수정, 삭제 등의 강제적인 작업을 하게 하는 공격 방법.

django는 최소한의 안전장치를 위해 자신이 부여한 랜덤 hash 값을 token 으로 부여한다. 이 token 값이 없는 요청은 잘못된 요청이라 판단하여 접근을 거부한다.(403 error)

django 가 해킹여부를 검증하는 방식 flask는 이런 위변조 보완 시스템을 따로 설정해줘야한다=micro framwork
```

```
1-2 정적파일:
image / css / js 파일과 같이 해당 내용이 고정되어 응답을 할 때 별도의 처리없이 '그대로 보여주기만 하면 되는 파일'들
```

```
1-3 URL 로직 분리 (프로젝트 url 하나로 모든 url을 관리 할 수 없으므로, 프로젝트 url은 상위 폴더 접근만 담당하고 각 폴더별로 따로 url 파일을 만들어준다.) 해당 파일에 접근할 때는 폴더명/파일명으로 접근

python manage.py startapp utilites 폴더생성

​```
# 최상위 프로젝트 urls.py 의 하위 폴더 url 관리

urlpatterns = [    
    path('utilities/', include('utilities.urls')),
    path('pages/', include('pages.urls')),
    # 최상위 프로젝트 폴더에 하위 폴더를 include해서 각 하위폴더가 직접 url 관리하고
    # 최상위 프로젝트 폴더는 하위 폴더에 처음 접근만을 관리
    # app 이름 + url ex) 127.0.0.1:8000/pages/index/ 로 바뀜
    path('admin/', admin.site.urls),  #항상 트레일링 컴마 , 를 붙이는 습관
]
```

```
1-4 Django namespace

'Django는 각 app의 templates폴더 까지는 읽어주는데, 거기에 경계를 두는 작업을 해야, 다른 앱, 같은이름의 html이 겹쳐도 각각의 app을 선택해서 경로를 들어갈 수 있도록 해줄 수 있다.(데이터가 많아질 경우 꼭 겹치는 제목이 생기므로)

pages 앱 폴더 안에 templates안에, **pages라는 폴더 (app폴더와 똑같은 이름)**를 새로 만들어서 그 안에 원래 templates 폴더에 있던 파일들(html)을 옮겨주어 다른 앱에 있는 같은 이름의 html과의 혼동을 방지한다.'

template / staitc이 프로젝트 폴더에 모두 모여있으니까 각 하위 폴더(appname)로 할당하는 방식으로 바꿔야함

기존: index.html > 이후: pages/index.html 로 접근 
```

```
setting.py > INSTALLED_APPS의 순서에 따라 파일이 실행된다.
따라서, 각 폴더의 pages > templates > pages / utilities > templates > utilities 폴더를 생성하여 namespace를 분리하여 파일에 각각 접근한다.(pages/index 등으로 세분화 하는것)

static 또한 pages파일을 만들어서 넣어주는 작업을 해준다.
 > pages > static > pages >images / stylesheets
 >> link rel="stylesheet" href="{% static 'pages/stylesheets/style.css' %}">
   <!-- 폴더 경로가 static으로 되어있므로 경로에는 static을 굳이 넣어줄 필요가 없다.  --> 
   
```
   # static 폴더 안에 위치한 파일을 사용할 경우 base.html 적용하는 방법
* base.html에
<head>
  {% block css %}
  {% endblock %}
</head>
--------------------------------
{% extends 'base.html' %}  
{% load static %}  

{% block css %}
  <link rel="stylesheet" href="{% static 'pages/stylesheets/style.css'%}">
{% endblock  %}

{% block content %}
<h1>Static 파일 실습</h1>
<img src="{% static 'pages/images/static.jpg'%}" alt="static_img">
{% endblock  %}
```

```
1-5 Template Inheritance(상속)

기본 프로젝트 폴더에 base.html 을 통해 모든 하위 폴더에 상속을 줘서 코드의 반복을 줄인다.
> 기본 프로젝트가 위치에 base,html 파일을 만들어서 하위 apps에 상속을 준다.

```
{% block ___ %}
{% endblock %} 주의
```

 <head>
 {% comment %} css 파일을 base.html 을 통해서 상속하기 위한 과정 > static_example {% endcomment %}
  {% block css %}
  {% endblock %}
 </head>

<body>
  <h1 class="text-center">Template Inheritance</h1>
  <hr>
  <div class="container">
  {% block content %}
  {% endblock %}
  </div>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

</body>
</html>


{% extends 'base.html' %}  >> 반드시 최상단에 있어야 한다 > base.html에 있는 내용을 하위 폴더로 상속하는 역할
```

```
오늘 배운 내용
1. Form (GET/POST)
2. POST - 주의사항: csrf_token
3. static(load, {% static '' %})
4. URL 로직 변경(프로젝트 & 앱)
5. django namespace(template, static) 장고가  템플릿과 스테틱을 한 곳에 모아두므로 폴더 별로 따로 공간을 설정해줌
6. 상속(block) > {% block ___%} ____이 동일해야한다.

