## FontAwesome

1. font awesome > kit url 받고 head 에 추가

```
<script src="https://kit.fontawesome.com/e1cb660948.js"></script>
```

2. font awesome animation I-lin .css 파일로 추가 및 link 연결 (https://l-lin.github.io/font-awesome-animation/)

```
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.2/animate.min.css">
```

```
Minified CSS for production usage > .css 파일 만들고 link로 연결
```

3. animate.css (font awesome 이외에 폰트에 사용)> view on github > readme 보고 cdn 설정

```
Example)

<h1 class="animated infinite bounce delay-2s">Example</h1>

infinite bounce -> rubberBand 등 원하는 걸로 바꿔서 사용
```

## FlexBox > 항상 display: flex; or d-flex와 같이 사용

- flex diction/wrap

```
display: flex; 기본값 
>>flex-direction: row; flex wrap: nowrap 
= flew-flow: row nowrap;

flex-direction: row / row-reverse / column / column-reverse  = 가로 세로 역방향
flex-wrap: nowrap / wrap / wrap-reverse = 넘치면 다음 줄로 넘어감
```

- 부모 요소인 .cointainer에 값 설정

```html
부모 값인 .container에 값을 그룹 선택자로 적용해야 자식 요소인 모든 items에 적용된다

.container {
  height: 100vh;
  border: 10px solid black;
  display: flex;
}

<div class="container p-0">
		<div class="item item1">1</div>
		<div class="item item2">2</div>
		<div class="item item3">3</div>
		<div class="item item4">4</div>
		<div class="item item5">5</div>
		<div class="item item6">6</div>
		<div class="item item7">7</div>
		<div class="item item8">8</div>
		<div class="item item9">9</div>
		<div class="item item10">10</div>
</div>
```

- flex grow

  ```html
  남는 좌우 여백을 5등분해서 지정한 클래스에 지정한 값 만큼 각각 나눠준다.
  (default = flex-grow: 0;)
  
  .items2 {
  flex-grow: 2;
  }
  
  .items3 {
  flex-grow: 3;
  }
  ```

- justify-content(가로축 조정)

```
justify-content: flex-start; -> 왼쪽정렬(default)
justify-content: flex-end; -> 오른쪽정렬
justify-content: center -> 가운데정렬
justify-content: space-between; -> 왼끝/중앙/오끝
justify-content: space-around; -> 여백 1221
justify-content: space-evenly; -> 여백 1111
```

- align-items(세로축 조정)

```
align-items: stretch;  -> 위아래 꽉차게(default)
align-items: flex-start;  -> 상단 정렬
align-items: flex-end;  -> 하단 정렬
align-items: center;  -> 가운데 정렬
align-items: baseline;  -> item의 상단에서 text 기준으로 줄 맞추기
```

- 개별 단위 움직임: align-self

```
.item8{
  align-self:flex-end;
}

.tiem5{
  align-self:center;
}
```

```
주의사항: direction-reverse 하는 순간, justify = y축, align = x축으로 사용된다.
x, y축으 바꿔서 지시해야한다.
```



- 순서지정 order

```
default = order:0
숫자가 작을수록 왼쪽으로 이동

.item2 {
   order: 1;
}

.item3 {
   order: -1;
}

.item5 {
   order: -2;
}

왼쪽부터 순서 5<3________<2
```

nav, aside, section, footer 등 <u>큰 틀</u>은 grid로 작성,

각 틀의 내부 요소는 flex box로 x, y 축 <u>세부조절</u>





