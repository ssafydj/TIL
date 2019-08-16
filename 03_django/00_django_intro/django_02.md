python -m venv venv

vs code: F1> python interpreter 'venv'로 이동 > pip list로 venv에 있는지 확인 

pip install django

django-admin startproject classroom .





```
vs code 켜는 방법

1. venv 설정 된 폴더 안에서 우클릭으로 vs code를 킨다.
2. Terminal이 켜있다면 끄고, F1 > venv로 이동한다.
3. Terminal을 켜면 source가 실행되어 있다.
```





```
csrf 사이트간 요청 위조

{% csrf_token %}

웹 어플리케이션 취약점 중 하나로 사용자가 자신의 의도와 무관하게 공격자가 의도한 행동을 해서 특정 웹페이지의 보안을 무력화 시키거나 수정, 삭제 등의 강제적인 작업을 하게 하는 공격 방법.

django는 최소한의 안전장치를 위해 자신이 부여한 랜덤 hash 값을 token 으로 부여한다. 이 token 값이 없는 요청은 잘못된 요청이라 판단하여 접근을 거부한다.(403 error)

django 가 해킹여부를 검증하는 방식 flask는 이런 위변조 보완 시스템을 따로 설정해줘야한다=micro framwork
```

 extension -> material icon theme 설치(아이콘 바뀜)

```
1-2 정적파일:
image / css / js 파일과 같이 해당 내용이 고정되어 응답을 할 때 별도의 처리없이 그대로 보여주기만 하면 되는 파일들
```

```
1-3 URL 로직 분리 (url 하나로 모든 폴더를 관리 할 수 없으므로, 처음 폴더 접근만 관리하고 각 폴더별로 따로 url 파일을 만들어준다.) 해당 파일에 접근할 때는 폴더명/파일명으로 접근

python manage.py startapp utilites 폴더생성
```

```
1-4 Django namespace

template / staitc이 한 곳에 모두 모여있으니까 각자 할당하는 방식으로 바꿔나가야함

index.html > pages/index.html 로 접근 
```

```
setting.py > INSTALLED_APPS의 순서에 따라 파일이 실행된다.
따라서, 각 폴더의 templates > pages 폴더를 생성하여 namespace를 분리하여 파일에 각각 접근한다.(pages/index 등으로 세분화 하는것)

```

```
1-5 Template Inheritance(상속)

기본 프로젝트 폴더에 base.html 을 통해 모든 하위 폴더에 상속을 줘서 코드의 반복을 줄인다.

        'DIRS': ['os.path.join(BASE_DIR, 'django_intro', 'templates')],
                                00_intro                                 까지 접근한다.
                                
                                
{% extends 'base.html' %}  >> 반드시 최상단에 있어야 한다. 
```

```
오늘 배운 내용
1. Form (GET/POST)
2. POST - 주의사항: csrf_token
3. static(load, {% static '' %})
4. URL 로직 변경(프로젝트 & 앱)
5. django namespace(template, static) 장고가  템플릿과 스테틱을 한 곳에 모아두므로 폴더 별로 따로 공간을 설정해줌
6. 상속(block) > {% block ___%} ____이 동일해야한다.
```





