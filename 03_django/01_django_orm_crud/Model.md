### 새로운 프로젝트 만들 때 마다

venv 켜고

프로젝트 만들고

앱만들고

setting.py에 앱 등록하고 시간대/언어 바꾸고

------------

## SQL (->Model)

## 모델의 개념

- 모델은 단일한 데이터에 대한 정보를 가지고 있다.

- 필수적인 필드(컬럼, 열)와 데이터(레코드, 행)에 대한 정보를 테이블에 포함한다.

  > 일반적으로 각각의 <u>모델(클래스)</u>는 단일한 데이터베이스 <u>테이블과 매핑(연동/연결)</u>된다.

- 모델은 부가적인 메타데이터를 가진 <u>DB의 구조(layout)를 의미</u>

- 사용자가 저장하는 데이터들의 필수적인 필드와 동작(behavior => 필드의 구체적 행동을 지정  ex) max_length)을 포함

  

Primary Key (기본키)= 데이터 고유값(중복x)

```
'ORM' : DB를 '객체'화 -> framework가 sql을 대신 지시/해석하게 도와줌 ex) 파이썬 코드로 작성하면 프레임워크가 sql 명령문으로 해석해줌 

즉, '객체를 조작하는 방법'을 알아야 ORM을 사용할 수 있다.

## ORM 사용 장/단점  (Object Relational Mapping)

# 장점
1. SQL 몰라도 DB 사용이 가능하다.
2. SQL의 절차적인 접근이 아닌 객체 지향적 접근이 가능하다.
3. 매핑 정보가 명확하여 ERD 를 보는 것에 대한 의존도를 낮출 수 있다.
>>ERD: 자료구조
4. ORM 은 독립적으로 작성되었기에, 해당 객체들을 재활용할 수 있다.(== Don't repeat your code) 
> 개발자는 객체에 집중함으로써 해당 DB에 종속될 필요없이 자유롭게 개발할 수 있다.

-----------------------

# 단점
1. ORM 만으로 완전하고 거대한 서비스를 구현하기가 어렵다.
> 즉, 사용하기는 편하지만, 설계를 신중하게 해야한다.
> 프로젝트의 규모가 커질 경우 오히려 난이도가 올라간다.
> 순수 SQL 보다 속도 저하가 생길 수 있다.
2. 이미 프로세스가 구축된 시스템에서는 ORM 으로 대체하기가 어렵다.(쓰려면 처음부터 써야한다)

------------------------

# 결론
> 큰 단점에도 불구하고 사용하는 이유 = 높은 생산성!
> 높은 생산성은 약간의 성능저하나 다른 단점을 상쇄하고 남음
> 장점 >>>>>>>>>>>>>>>>>>>>단점 이기에 대부분의 프레임워크들이 ORM을 사용하고 있다.

즉, 우리는 DB 객체(object)를 -> 인스턴스(instance)로 조작하기 위해 ORM을 배운다.
(OOP의 개념을 깊이 이해하자 -> 클래스, 인스턴스, 메서드 등)
```



파이썬를 이용하여 객체형태로 ORM을 작성한 후,  장고로 보내면 알아서 SQL로 해석해서 표를 만들어줌



## 필드설명

Docs: https://docs.djangoproject.com/en/2.2/ref/models/fields/#primary-key

1. CharField()

   - 길이에 제한이 있는 문자열을 넣을 때 사용
   - max_length 는 필수 인자이다.
   - 필드의 최대 길이(문자)이며, DB 그리고 django 의 유효성검사(값을 검증)에 사용됨
   - 텍스트 양이 많을 경우 'TextField()'로 사용

2. TextField()

   - 글자 수가 많을 때 사용

   - max_length 옵션을 줄 수 있지만 모델과 실제 DB에는 적용되지 않는다.

     > 길이 제한을 주고 싶다면 CharField() 를 사용해야 한다.

3. DateTimeField()

   - 시간과 날짜를 기록하기 위한 필드
   - auto_now_add=True
     - django ORM 이 '최초 INSERT(테이블에 데이터 입력)시에만' 현재 날짜와 시간 작성
     - **최초 생성 일자**
   - auto_now=True
     - django ORM 이 SAVE 를 할 때마다 현재 날짜와 시간 작성
     - **최종 수정 일자**



## model 로직  

- DB column과 어떠한 타입으로 정의할 것인지에 대해 django.db 모듈의 models 의 상속을 받아서 적용된다.

  > from django.db import models

- 각 모델은 **'django.db.models.Model' 클래스의 서브 클래스**로 표현된다.(자식 클래스) 

  > -> 이미 만들어놓은 클래스를 models.Model로 상속받아서 가져다 쓰면됨

  > https://github.com/django/django/blob/master/django/db/models/base.py  line 400~1800

- 모든 필드는 **기본적으로 NOT NULL 조건**이 붙는다(DB에는 NULL 값이 들어갈 수 없다) -> DB의 무결성

- 각각의 **클래스 변수들은 모델의 데이터베이스 필드**를 나타낸다.



## Migrations  (db. 파일은 gitignore에 해당되기에 다른 컴퓨터에서 clone 후에는 따로 migrate 해야한다)

sqlite 설치 -> F1 > sqlite > open database > db.sqlite 3 > 왼쪽 사이드바에 sqlite explorer 생성됨

```
sqlite3 홈페이지 > 
Precompiled Binaries for Windows
sqlite-dll-win64-x64-3290000.zip
(788.61 KiB)		64-bit DLL (x64) for SQLite version 3.29.0.
(sha1: c88204328d6ee3ff49ca0d58cbbee05243172c3a)
sqlite-tools-win32-x86-3290000.zip
(1.71 MiB)		A bundle of command-line tools for managing SQLite database files, including the command-line shell program, the sqldiff.exe program, and the sqlite3_analyzer.exe program.
(sha1: f009ff42b8c22886675005e3e57c94d62bca12b3)

2개 폴더 설치
> C 드라이브에 sqlite 폴더 만들고 압출 푼 파일 5개를 넣어준다

시스템 환경변수 설정에 path에 시스템 변수 path에 C:\sqlite 새로만들고 
git bash 를 켜서 

$ winpty sqlite3 로 켜지는 확인
.exit 로 나가기

code ~/.bashrc 켜서 아래 복붙

export FLASK_ENV=development
alias jp="jupyter notebook"
alias venv="source ~/python-virtualenv/3.7.3/Scripts/activate"
alias sqlite3='winpty sqlite3'

git bash에서 source ~/.bashrc 로 활성화하고 변경한 단축어인 sqlite3 로 작동하나 확인하기

vs code 다시 켜서
가상환경 켜고
sqlite3 db.sqlite3 작동하나 확인
킨 상태에서 .tables 입력하면 기존에 만들어 놓은 테이블들 목록 확인가능

.schema articles_article 입력하면 아티클 속성 확인가능
```



> 이후에 python manage.py migrate 를 시행하고  > 많이 설치됨(setting.py > install_apps 에 있는 모든 항목 + 0001, 0002가 설치되었기 때문 )

1. migrations  > django가 생성한 파일은 절대 변경하면 안된다. 필요하다면 삭제 후 다시 진행

   - 모델(model.py) 작성/변경 사항을 django 에게 알리는 작업(ORM에 보낼 python **코드 설계도를 작성**)

     > python manage.py makemigrations 

     - migrations 폴더 안에 0001.py 파일이 생성됨

     > python manage.py sqlmigrate 0001

     - 어떻게 테이블을 만들지 보여줌

     > python manage.py makemigrations 

     - 새로운 model update  하면 새로운 0002_ 파일이 만들어진다. dependencies 를 통해 상속된 내용과 operations를 통해 업데이트 된 내용을 확인

   - 테이블에 대한 설계도(django ORM이 만들어줌)를 생성

     

2. migrate

   - migrations 로 만든 설계도를 기반으로 실제 <u>db.sqlite3</u> DB에 반영한다 .

   - <u>models.py 에서의 변경사항들과 DB 스키마가 동기화</u>를 이룬다.

     

ORM_tablename 으로 테이블이 만들어짐



```
1. migrations
> $ python manage.py makemigrations = 모델(model.py)을 작성/변경한 사항을 django 에 알리는 작업
```

### 추가사항

```
$ python manage.py sqlmigrate app_name 0001
> 해당 migrations 설계도가 SQL 문으로 어떻게 해석되어서 동작할지 미리 볼 수 있다.(필수사항x)
```

```
$ python manage.py showmigrations 
> migrations 설계도가 migrate 됐는지 안됐는지 [X] or []를 통해 확인한다(필수사항x)
```



### Model *****변경 시 *작성 *순서 

1. models.py: 작성 및 변경(생성/수정하는 공간)
2. makemigrations: migrations 파일 만들기(설계도 작성) > python manage.py makemigrations
3. migrate: 실제 DB에 적용 및 동기화(테이블이 생성됨) > python manage.py migrate

---------------------

테이블의 이름은 app 이름과 model 에 작성한 class 이름이 조합되어 자동으로 만들어진다(<u>** 모두 소문자**</u>)

모델의 클래스변수들은 반드시 **소문자**로 작성한다.



### CRUD (DB API 조작)

> > Create Read Update Delete -> 모든 웹의 필수 동작 단계

1. django Shell 

   - django 프로젝트 설정이 로딩된 파이썬 shell

   - 일반 파이썬 shell 로는 django 환경에 접근 불가하므로 django shell 을 사용
   - 즉, django 프로젝트 환경에서 파이썬 shell 을 활용한다고 생각하면 됨

   > pip install ipython 설치 (shell 시각화(컬러링) 용도)

   - shell 켤 때  -> python manage.py shell
   - from articles.models import Article             articles = app 이름 // Article = class 변수이름
   - Article.objects.all()

   

   #### admin 설정
   
   > python manage.py createsuperuser
   

   
   
   
   - 테이블 내용을 전부 조회(READ)
     - DB 에 쿼리를 날려서 인스턴스 객체 전부를 달라고 하는 뜻
  - 만약에 레코드가 하나라면, 인스턴스 단일 객체로 반환
     - 두 개 이상이면, QuerySet 형태로 반환

   >  (ORM)Article.objects.all()  > 사용자가 작성하는 내용 (READ 할 떄 쓰는 ORM 문법)
>
   > == 
   >
   > (SQL)SELECT*FROM articles_article;  > DB가 이해하는 내용

   

## 1. CREATE

- QuerySet 기본 개념
     - 전달 받은 객체의 목록
    - QuerySet: 쿼리 set 객체
       
       - Query: 단일 객체
     - DB 로부터 데이터를 읽고, 필터를 걸거나 정렬 등을 수행
    - Query 를 던지는 Language(django ORM) 를 활용해서 DB에게 데이터에 대한 조작을 요구한다.
       
   
      
   
   QuerySet
   
   - Objects를 사용하여 **<u>다수의 데이터를 가져오는 함수를 사용할 때 반환되는 객체</u>**
   - 단일한 객체를 반환(return)할 때는 테이블(class)의 인스턴스로 반환된다.



​		objects

   - Model manager 와 django Model 사이의 query 연산의 인터페이스(중간다리) 역할을 해줌

   - 즉, models.py에 설정한 클래스(테이블)을 불러와서 사용할 때 DB 와의 인터페이스 역할(쿼리를 날려주는)하는 매니저이다.

   - 쉽게 이해하려면 ORM 의 역할이라고 생각하면 된다.

   - DB ------------------ objects ----------------------------- Python Class(models.py)

   - Manager(objects) 를 통해 특정 **<u>데이터를 조작(메서드)</u>**할 수 있다. 

     > all() -> 내용을 전부 불러오는 메서드

----------------------------

```
OOP개념과 클래스, 메서드로 테이블 내용을 채우자

article = Article()
article.title = 'first'
article.content = 'django!'
article.save()   # 데이터 저장
Article.objects.all() # 저장된 내용을 확인 및 article.title 식으로 입력하여 내용확인가능

> sqlite3 open data 해서 확인하면 article_article에 테이블이 추가된 것을 확인가능
```



### 데이터 객체를 create 하는 3가지 방법

1. 첫번째 방식 (일반적으로 사용하는 방식 1)

   ```
   $ python manage.py shell
   
   #SQL : 특정 테이블에 새로운 레코드(행)를 추가하여 데이터 추가
   # INSERT INTO TABLE (Column1, Column2, .....) VALUES(value1, value2, ...)
   # INSERT INTO articles_article (title, content) VALUES ('first', 'django!') 
   
   <=======>
   
   #ORM
   >> article = Article()   # Article class 로부터 article 인스턴스 생성
   >> article.title = 'first'  # 인스턴스 변수(title)에 값을 할당
   >> article.content = 'django!' # 인스턴스 변수(content)에 값을 할당
   
   즉, 사용자가 ORM으로 작성하면 django 에서 SQL 문으로 해석해준다.
   
   # save를 하지 않으면 아직 DB에 값이 저장되지 않음
   >> article
   <Article: Article object (None)>
   >> Article.objects.all()
    	<QuerySet []>
   
   # save 후에 확인해보면 저장된 것을 확인할 수 있다.
   >> article.save()
   >>article
   >>Article.objects.all()
     <QuerySet [<Article: Article object (1)>]>
     
     
   # 인스턴스 article 을 활용하여 변수에 접근할 수 있다.(저장된 값 확인)
   >> article.title
   'first'
   >> article.content
   'django!'
   ....
   ```

2. 두번째 방식 (일반적으로 사용하는 방식 2)

```
>>> article = Article(title='second', content='django!!')
>>> article.save()
```

3. 세번째 방식

   - create() 를 사용하면 쿼리셋 객체를 생성하고 저장하는 로직이 한 번의 스텝으로 끝난다.

     > 유효성 검정없이 바로 저장하므로 create()는 잘 사용하지 않는다

```
>>> Article.objects.create(title='third', content='django!!!')
```

#### 유효성 검사

- save 전에 'full_clean()' 메서드를 통해 article 이라는 인스턴스 객체가 검증(validation)에 적합한지를 알아볼 수 있다. 
- models.py 에 필드 속성과 옵션에 따라 검증을 진행한다.

--------------------------------

### READ(creat 한 내용을 read)

```
# 1. SELECT * FROM articles_article;
# 1. DB 에 있는 모든 글 가져오기
>>> Article.objects.all()

# 2. SELECT * FROM articles_article WHERE title='first';
# 2. DB에 저장된 글 중에서 title 이 first 인 글만 가져오기
>>> Article.objects.filter(title='first')

# 3. SELECT * FROM articles_article WHERE title='first' LIMIT 1;
# 3. DB 에 저장된 글 중에서 title이 first인 글 중에서 첫번째 글만 가져오기
>>> Article.objects.all().first()
>>> Article.objects.all().last() # 마지막 값


# 4-1. SELECT * FROM articles_article WHERE id=1;
# 4-1. DB 에 저장된 글 중에서 pk 가 1인 글만 가져오기  
>>> Article.objects.get(pk=1)

# pk 만 .get() 으로 가져올 수 있다. (.get() 은 값이 중복이거나 일치하는 값이 없으면 에러를 발생시킴) 즉, pk 에만 사용하자!

# 4-2. filter 의 경우 존재하지 않으면 에러가 아닌 빈 쿼리셋을 반환한다. 마치 딕셔너리에서 value 를 꺼낼 때 [] 방식으로 꺼내는지 또는 .get 으로 꺼내는지의 차이와 유사한 문제
>>> Article.objects.filter(pk=100)
<QuerySet []>

# 4-3. filter / get
# filter 자체가 여러 값을 가져올 수 있기 때문에 django 가 갯수를 보장하지 못한다. 따라서 0개, 1개라도 무조건 쿼리셋으로 반환한다.


# 5-1. 오름차순(default)
# SELECT * FROM articles_article ORDER BY title ASC;
>>> Article.objects.order_by('pk')

# 5-2. 내림차순
# SELECT * FROM articles_article ORDER BY title DESC;
>>> Article.objects.order_by('-pk')

# 6. 쿼리셋은 LIST 자료형은 아니지만, list에서 할 수 있는 인덱스 접근 및 슬라이싱이 모두 가능하다.
>>> Article.objects.all()[2]
>>> Article.objects.all()[1:3]

# 7. LIKE / startswith / endswith
# django ORM 은 이름(title)과 필터(contains)를 더블언더스코어(__)로 구분한다.
# 더블언더스코어 ==> 던더(dunder)스코어

#LIKE
>>> Article.objects.filter(title__contains='fir')

# startswith
>>> Article.objects.filter(title__startswith='fir')

# endswith
>>> Article.objects.filter(title__endswith='!')
```

### UPDATE

```
# article 인스턴스 객체의 인스턴스 변수에 들어있는 기존 값을 변경하고 저장
>>> article = Article.objects.get(pk=1)  # 1. 특정 article 선택
>>> article.title = 'byebye'  # 2. 변경
>>> article.save() -> # 바뀐 값을 table 에 3. 저장
```

### DELETE

```
# article 인스턴스 객체를 생성 후 .delete() 메서드를 호출
>>> article = Article.objects.get(pk=1)

>>> article.delete()
```

- 핵심: 우리는 ORM 을 통해 클래스의 인스턴스 객체로 DB 를 조작할 수 있다.
- 앞으로 CRUD 로직을 직접 작성하면서 위에서 배운 코드들을 다시 활용할 것 이다.

--------------------

## ADMIN

Docs: https://docs.djangoproject.com/en/2.2/ref/contrib/admin/

- 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지

- models.py 에 작성한 클래스를 admin.py 에 등록하고 관리한다.
- record 생성 여부 확인에 매우 유용하고, 직접 레코드를 작성할 수도 있다.
- CRUD 로직을 모두 관리자 페이지에서 사용할 수 있다.



### 관리자 변경 목록(change list) 커스터마이징

1. **list_display**

   - admin 페이지에서 우리가 models.py 에 정의한 각각의 속성(컬럼)들의 값(레코드)을 보여준다.

2.  list_filter

   - 특정 필드에 의해 변경목록을 필터링 할 수 있게 하는 filter 사이드바를 추가한다.

   - 표시되는 필터의 유형은 필드의 유형에 따라 다르다.

3. list_display_links

   - 목록 내에서 링크로 지정할 필드 적용(설정하지 않으면 기본값을 첫 번째 필드에 링크가 적용)

4. list_editable

   - 목록 상에서 직접 수정할 필드 적용

5. list_per_page

   - 한 페이지에 표시되는 항목 수를 제어(기본값: 100)

--------------------

## Django extensions

docs: https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#installation

- Django-extension 은 커스텀 확장 tool 이다.
- Django app 구조로 되어 있기에 프로젝트에 사용하기 위해서는 app 등록 과정이 필요하다



