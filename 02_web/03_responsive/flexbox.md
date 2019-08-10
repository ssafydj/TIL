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

## FlexBox

```
display: flex; 기본값 
>>flex-direction: row; flex wrap: nowrap 
= flew-flow: row nowrap;

flex-direction: row / row-reverse / column / column-reverse  = 가로 세로 역방향
flex-wrap: nowrap / wrap / wrap-reverse = 넘치면 다음 줄로 넘어감
```





*container: 부모(상위 요소)

*flex items: 자식

 (정해진 이름은 아님)



nav, aside, section, footer 등 <u>큰 틀</u>은 grid로 작성,

각 틀의 내부 요소는 flex box로 x, y 축 <u>세부조절</u>



```
<u>x축 justify</u>  w/ content

<u>y축 align</u> w/ items or self



한줄 items

여러줄 content

개별요소 self

-> <u>조합</u>해서 사용하면 된다.



!! direction 을 reverse 하는 순간, justify = y축, align = x축으로 사용된다.
```

