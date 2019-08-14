## python을 잘해야 django를 잘 사용한다.  

기본목적: template(.html) 을 사용자에게 보여주기위함. > 가능한 모든 계산 및 처리는 views에서 한다.

## web application tool / 서버

> > > 파이썬으로 짜여진  framework이다.

> > > 독선적인 framework = 엄격한 룰 > 장: 룰을 잘 따르면 쉬운 개발(높은 생산성), 단: 개발자의 자유하락 

> > 시스템 환경변수 편집> 환경변수 > path > python 3.7 위로 이동

- 가상환경을 사용하는 이유(모든 setting을 동일하게 만들기 위함)

  의존성: 

  > 내 컴퓨터에서 잘 작동하던 프로그램이, 다른 컴퓨터에서도 잘 작동한다는 보장이 없음

  > 또한, 같은 버전의 파이썬과 모듈을 쓴다는 보장이 없다.

  > 특정 프로그램만을 실행하기 위한 파이썬 환경을 따로 만들어서, 그 환경에서만 모듈을 관리하고 앱을 실행 시키기 위해 가상환경을 설정한다.

  > 다른 앱을 실행시키면 그 가상환경을 빠져나와 다른 환경을 만드는  방식으로 진행한다.

  - 가상환경 만드는 방법	

    > python -m venv (가상환경 경로+이름)
    >
    > > ex) python -m venv ssafy

  - gitignore.io > django, vscode

  00_django_intro 폴더 안에서: 

  git bash로 python -m venv venv

  (vene 활성화/폴더 생성됨)

  source venv/Scripts/activate   = 가상환경 on

  (pip list 찍어보면 > 2개뿐)

  deactive = 가상환경 off

  (pip list 찍어보면 > global에 설치된 pip 엄청 많음)

  

  ```
  # 항상 vs code로 django 시작할 때 
  
vs code 에서 F1켜서  python: select interpreter에서 3.7 venv: venv로 변경
  
![1565743550743](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1565743550743.png)
  
  vs code 좌하단에 이 표시가 없으면 <u>가상환경에 접속</u> 안한것이다.<>global 
  
  (terminal에서 pip list로 가상환경에 위치하고 있는지 다시 확인)
  ```
  
  pip install django  (장고 설치)
  
  python -m django --version (version 확인)
  
  
  
  django-admin startproject django_intro .   ( .설정해서 불필요하게 2중폴더 만들지말자!)

  

  python manage.py runserver (설치시 위치 주의) 

  (student@DESKTOP MINGW64 ~/Desktop/TIL/03_django/00_django_intro (master)에서 설치)

  

  ----------------------설치완료--------------------------

  ctrl + c = 종료 

  

  ```
- - app 만들때 (app의 이름은 pages와 같이 <u>복수형</u>으로 만든다)
  
  > > > python manage.py startapp pages
  
project 폴더 안에 setting.py에 install_appes 에 필요한 클래스를 등록해준다.
  
​```
   'pages.apps.PagesConfig',
​```
  
setting.py 하단에서 language code를 'ko-kr'
  
​								Time-zone을 	'Asia/Seoul'로 변경
  ```

  

  현대 framework 기본구조/패턴: <u>MVC</u> (model view controler) contoler가 model에 접근하고 view에 뿌려주고  

  실행순서: urls>view>template>user 

  플라스크의 기능을 하나하나 독립시킨 개념

  django: MTV (model template view)  데이터를 관리 / 사용자가 보는 화면 / 중간 관리자(요청받고 뿌려줌)

  

  


## TV 작동

1) view 짜기

2) url 만들기    > 사용자가 image라는 주소에 들어갔을 때 image를 view함수로 보여준다!

3) url통해서 rendering 된 순간 tempelates에 있는 index.html로 연결하여 사용자에게 보여줌



> ```
> #urls.py 설정
> 
> from pages import views
> 
> urlpatterns = [
>  path('index/', views.index),
>  path('admin/', admin.site.urls),
> ]
> 
> url을 통해 만들어놓은 index/ 주소를 views.index를 연결시켜주는 역할
> ```
>
> 

url말고 view 먼저 짜는 이유: url 짤 때  views를 연결할 index를 먼저 만들고 url을 입히는게 나아서.







- 코드 작성 순서

  ```
  1. views: 만들고자 하는 view 함수 작성
  2. urls: views 에서 만든 함수에 주소를 연결
  3. templates: 해당 view 함수가 호출 될 때 보여질 페이지 작성
  ```

  - vs code 설정 (setting.json에)

    ```
    1. django
    extension 에서 django 설치 > repository 가서
        "files.associations": {
            "**/*.html": "html",
            "**/templates/**/*.html": "django-html",
            "**/templates/**/*": "django-txt",
            "**/requirements{/**,*}.{txt,in}": "pip-requirements"
        },
        "emmet.includeLanguages": {"django-html": "html"},
        
    2. beatufiy
    extiositon> beaytify > repository 가서
    "beautify.language": {
          "js": {
            "type": ["javascript", "json"],
            "filename": [".jshintrc", ".jsbeautifyrc"]
            // "ext": ["js", "json"]
            // ^^ to set extensions to be beautified using the javascript beautifier
          },
          "css": ["css", "scss"],
          "html": ["htm", "html", "django-html"]
          // ^^ providing just an array sets the VS Code file type
        }
    
    붙이기
    ```

    

- 동적 라우팅  -> 주소자체를 변수처럼 사용 request 이외에 다른 변수가 필요

  (변수 이외에 추가하여 주소를 구분할 변수)

  기존의 context에 변수를 추가하여 자유롭게 사용할 수 있다.

  ```python
  def hello(request, name):
      menu = ['족발', '햄버거', '짬뽕', '덮밥']
      pick = random.choice(menu)
      context = {'name': name, 'temp_pick': pick}  # context에 변수를 자유롭게 추가해서 사용가능
      return render(request, 'hello.html', context)
  ```

  

  

  - Django Template Language(DTL)
    - django template 에서 사용하는 내장 template system 이다.
    - 조건, 반복, 변수, 치환, 필터 등 많은 기능을 제공한다.
    - 

  