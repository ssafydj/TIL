1. 들여쓰기는 공백 2문자를 사용

   >  ctrl ship p > open setting .json
   >
   > "[html]": {
   >
   > ​        "editor.tabsize": 2
   >
   > ​    },
   >
   > ​    "[css]": {
   >
   > ​        "editor.tabSize": 2
   >
   > ​    }

   + 속성명들은 모두 붙혀서 작성한다.(no space)

2.  속성 값에는 반드시 '큰 따옴표'를 사용

3. 태그, 속성, 속성값 등에는 모두 소문자만 사용한다.

4. 최상위 html 태그에는 lang 속성을 주어 문서의 기본 언어를 지정한다.

   (web 접근성 목적: 스크린 리더는 lang을 통해 언어를 인식하여 자동으로 음성을 변환하거나 해당 언어에 적합한 발음을 제공한다.)

5. IE의 경우에는 특정 META 태그를 사용해 페이지가 특정 버전에 맞게 세팅 되도록 지정해준다.

```python
<meta http-equiv="X-UA-Compatible" content="ie=edge">
```

6. boolean 속성 값은 따로 명시하지 않는다.

   ```html
   <good></good> 
   <input type="radio" name="bread" value="1" checked>에그 마요<br>
   
   <bad></bad>
   <input type="radio" name="bread" value="1" checked=TRUE>에그 마요<br>
   ```
```
시맨틱 태그 에서 포함범위: section > article 

> 시맨틱: ''검색엔진 최적화''라는 개념으로 관련된 정보를 같이 제공하는 개념으로 마케팅에서 중요

시맨틱 태그의 순서를 지키면 깔끔하고 좋은거지, 안지킨다고 작동안하는거아님.

네이버 vs 카카오톡

> 네이버: 시맨틱 태그 O header tag로 설정해놓음
>
> 카카오톡: x

chrome extetion: web developer (톱니바퀴) 설치



vs code 'beautify' 설치 >styleguide에 맞게 정렬해줌

'preferences: open keyboard shortcuts' 에서 beautify, 단축키설정

---------------------------

02index h1 태그는 1개만 사용, 나머지는 자유롭게 사용하되, 형식 중시

bold <> strong : 나타나는건 같지만, semantic 의미론적으로 strong이 작동함 bold는 작동x ex) 스크린리더
```