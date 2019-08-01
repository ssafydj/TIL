### CSS -HTML에 디자인을 적용



{} 사용

한 줄이 끝날 때마다 항상 ; 붙히기

form: 셀렉터{프로퍼티:값 ;프로퍼티:값} 

프로퍼티 값의 단위: 

1. 키워드 
2. 크기단위: px(디바이스별로 픽셀의 크기는 제각각), %(ex)width), em(같은 값이더라도 값이 다를수있다.), rem(값이 같음), viewport (vw /vh 너비 높이의 움직임에 맞게 변화한다: 반응형 디자인)
3.  색깔

1. Inline 방법: HTML 요소의 syle에 css를 넣기

```html
<body>
  <h1 style="color: rosybrown;">inline css 적용</h1>
</body>
```

스타일 적용 우선순위(1>2>3)

1. embedding: HTML 내부에 CSS를 포함시키기(특수한 경우에만 사용)

   1<>2 동일한 방법 but 위치만 다름

2. link file(외부참조): link tag로 css와 html 을 연결

   ```html
   <body>
     <h1 style="color: rosybrown;">inline css 적용</h1>
     <h2>내부참조, embedding</h2>>
     <h3>외부참조, file link</h3>
   </body>
   
   <h2>내부참조, embedding</h2>>
   ```

3.  

   ```
   <h3>외부참조, file link</h3>
   #별도의 css 파일을 만들어서 아래 입력
   h3 {
     color: rgb(202, 39, 161);
   }
   ```

   

- 컴포넌트화: 공통되는 부분은 하나로 묶고(ex)사이즈) 서로 다른부분은 각기 설정 



선택자 우선순위

0. !importatnt

1. 인라인 스타일
2. 아이디 선택자
3. 클래스 선택자

4. 태그선택자

5. 전체선택자



## css 스타일 가이드

기준: https://ui.toast.com/fe-guide/ko_HTMLCSS

1. 들여쓰기 2문자

2. 클래스, 아이디명은 케밥 케이스(kebob-case)

3. 콜론 이후에는 공백

4. 다중 선택 시 한 줄에 선택자를 하나씩 작성

   ```css
   .bold,
   .yellow,
   .bold {
     font-weight: bold;
   }
   ```

    

5. 모든 스타일 뒤에는 세미콜론;을 붙인다.

6. 스타일 지정할 때 아이디, 태그 대신에 클래스를 사용한다.(되도록, 대부분)

   (id는 딱 하나만 지정가능, 클래스는 함수처럼 만들어놓으면 다중으로 할당가능. 클래만 사용하면 우선순위 따질필요x)

7. 숫자 0 이후에는 불필요한 단위를 작성하지 않는다. ex)0 > 0px 
8. google font 불러올 때, @import 대신 <link> 방법을 사용한다.
9. 가능하면 단축어(축약형)를 사용한다. (단, 불필요하게 사용하는 것은 지양한다.)

## box model

css의 모든 것은 사각형. 원이 있다면 사각형을 돌려 깎아서 만든거임

margin-top: 10px; 라면 bottom 으로 10px 이동한다는 것.

1. 상하좌우

2. 상하 / 좌우

3. 상 / 좌우 / 하
4. 시계방향



* emmet: class id select 개념이 합해진 생산성 높여주는 기술  div.content-box+div.border-box
* lorem ipsum 10 = dummy text 로 미리 10 단어 출력값을 확인해볼 때 사용하는 기술



box-sizing: content box vs border

content(default): content 를 기준

border:  border 기준이므로 padding이 늘어나도 일정 넓이(설정하는 크기에 따라 다름)까지는 깨지지않음

따라서 border box를 기본값으로 설정하고 시작해라!



1. blcok: 화면 전체의 가로폭을 차지한다. ex) h1 heading 너비가 정해지면 나머지는 margin으로 처리

> 좌 우 중간 정렬에 활용된다

2. inline: 새로운 라인에서 시작하지 않으며 문장의 중간에 들어갈 수 있다. ex)span > 자신의 컨테츠만큼은 공간만 차지한다.
3. inline-block: 2번의 단점인 width, height 등의 특징을 사용할 수 있도록 2번의 단점을 보완
4. None: 해당요소를 화면에 표시하지 않는다.(공간조차도 사라진다)



- cover

 배경 이미지의 크기 비율을 유지한 상태에서 부모 요소의 width, heigh 중 큰 값에 배경이미지를 맞춤.

따라서, 이미지의 일부가 보이지 않을 수 있다

- contain

배경이미지의 크기 비율을 유지한 상태에서 부모 요소의 영역의 배경이미지가 보이지 않는 부분가지 전체가 들어갈 수 있도록 이미지 크기를 조절한다.

- attachment: fixed

화면이 스크롤 되더라도 배경 이미지는 스크롤 되지않고 고정시킨다.

```
bagkground-size cover 
			position center 속편하게 이미지 맞추는 팁
```

