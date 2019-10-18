### URI

- 인터넷에 자원을 나타내는 유일한 주소
- 인터넷에서 요구되는 기본조건으로서  http에 항상 붙어 다닌다.

### URL

- 인터넷 상에서 자원이 어디 있는지 알려주기 위한 규약



### 예제

1. https://www.google.com

   > 서버주소(URL 이면서 URI 이다)

2. https://github.com/seasign10/STUDY/blob/master/01_Startcamp/190710_study2_HTML_CSS.md

   > 주소 + 디렉토리 파일의 주소(자원의 위치)
   >
   > URL 이면서 URI

3. [https://www.google.com/search?q=%EC%82%BC%EC%84%B1](https://www.google.com/search?q=삼성)

   > 주소 + 특정 문자열(query string) -> search?q=
   >
   > search 까지가 URL + q=삼성 이라는 식별자가 필요하므로 URI 이지만 URL은 아니다.



GET POST PATCH DELETE

실제로 HTTP 에서는 공식적으로 GET POST 만 공식적으로 사용된다.



GET articles/create/ -> 글을 작성하는 페이지

POST articles/create/ -> 글이 실제로 작성되는 페이지



같은 주소로 들어가는데 GET OR POST 에 따라 다르게 행동할 것이다. (NEW+CREATE)



form tag 에 action 이 없다면, 현재 머물고 있는 URL 로 요청을 보낸다.



### Model Instance Method

1. get_absolute_url()





### URL Reverse 를 수행하는 함수들

### 1. reverse()

- 리턴 값: string

  ```
  reverse('articles:index') # '/articles/'
  ```

### 2. redirect()

- 리턴 값: HttpResponseRedirect(객체)
- 내부적으로 resolve_url() 을 사용
- view 함수에서 특정 url 로 돌려보내고자 할 때 사용

```
redirect('articles:article')
## <HttpResponseRedirect status_code=200, "text/html; charset=utf-8, url="/articles">
```

### 3. url template tag({% url %})

- 내부적으로 reverse() 를 사용



redirect(모델 인스턴스)를 통해서 모델 인스턴스의 get_absolute_url() 함수를 자동으로 호출

