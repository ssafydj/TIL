fontawesome > kit url 받고 head 에 추가, 

font awesome animation I-lin .css 파일로 추가 (https://l-lin.github.io/font-awesome-animation/)

animate.css (font awesome 이외에 폰트에 적용할 때)> view on github readme 보고 cdn 설정

```
<head>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.2/animate.min.css">
</head>
```

```
example of usage)

<h1 class="animated infinite bounce delay-2s">Example</h1>

infinite bounce -> rubberBand 등 원하는 걸로 바꿔서 사용
```





## Flex box

*container: 부모(상위 요소)

*flex items: 자식

 (정해진 이름은 아님)



nav, aside, section, footer 등 큰 틀은 grid로 작성,

각 틀의 내부 요소는 flex 로 x, y 축 세부조절



x축 justify  w/ content

y축 align w/ items or self



한줄 items

여러줄 content

개별요소 self

-> <u>조합</u>해서 사용하면 된다.



!! direction 을 reverse 하는 순간, justify = y축, align = x축으로 사용된다.