### Bootstrap (front-end framework / library)

bootstrap와  CSS를 보완적으로 사용함.

HTML vs bootstrap > 깔끔하고 세련됨

```html
설치: bootstrap > documentation> download css js 복붙
```

```html
<head>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>

<body>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>
```

CDN: 별도의 파일을 다운로드 할 필요없이  link를 통해 데이터를 쉽고, 빠르고, 데이터 소모없이 사용하게함. (=적절한 수준의 캐시설정으로 빠르게 로딩할 수 있다.) content delivery network



* ''*<u>클래스</u>'' *로 동작한다.  

  ```
  bootsrap 기본 작동법
  
  . = 클래스로 접근
  - = 구체적인 값을 할당 또는 font-weight-bold 등 font에서 font-weight로 접근 
  ```

* <u>이미 bootstrap에 만들어진 class name 을 자유롭게 활용하면 된다.</u>

  ```
  .css 파일이 따로 필요없으므로, <head>에 <style>형식으로 자주쓰는 div, img 등 틀을 만들어서 사용하면 된다.
  
  <style>
      div {
        width: 100px;
        height: 100px;
      }
  
      img {
        width: 500px;
        height: 300px;
      }
  </style>
  ```

  

```
**margin
margin:0;   .m-0  상하좌우0
 > <div class="m-0">margin 0</div>

margin-right:0    .mr-0 우0

margin-left/right:  .mx-0 좌우(x축)0

**padding
padding:-0;			.p-0
padding-right:0;	.pr-0	
padding-top/bottom:0  .py-0 패딩 상하(y축)0


## 브라우저 기본 rem은 16px 
## spacer(1rem)*0.25 = 16px*0.25 = 4px 

.mt-1   margin-top:0.25rem  4px
.mt-2	margin-top:0.5rem	8px
.mt-3						16px
.mt-4						24px
.mt-5						48px

.mx-auto (좌우를 이동) = 가운데 정렬

etc...
```

```html
##color
.bg-primary		blue
.bg-secondary	grey
.bg-success		green
.bg-danger		yellow
.bg-warning		red
.bg-info		sky-blue
.bg-light		opaque
.bg-dark		black
.bg-white		white

##color 활용법
.text-success -> 초록색 text
.alert-warning -> 노랑색 alert
.btn-secondary -> 회색 button
.navbar-dark.bg-primary -> 2개 이상 요소를 .으로 연결해서 사용가능
.border.border-success -> 초록색 border
> <div class="border border-primary">경계가 파란색</div>

##display
.d-block
.d-inline
.d-inline-block
.d-none

##display 응용
<!-- div는 원래 block 이지만, inline 으로 만들 수 있다 -->
  <div class="d-inline bg-primary text-white">div to inline</div>
  
<!-- span은 원래 inline 이지만, block 으로 만들 수 있다. -->
  <span class="d-block bg-info text-white">span to block</span>
  
##position
.position-static
.position-relative
.position-absolute
.position-fixed

<!-- position fixed =sticky-->
<style>
 .sticky {
  width: 100%;
  height: 20px;
 }
</style>
<body>
  <div class="sticky fixed-top bg-dark"></div>
</body>


```

```html
text-align: center 		.text-center
text-align: left		.text-left
text-align: right		.text-right

font-weight: bold		.font-weight-bold

image 파일을 불러와서 .rounded-circle/pill로 모서리를 깍아서 사용
<img src="images/ssafy.png" alt="#" class="rounded-circle">
<img src="images/ssafy.png" alt="#" class="rounded-pill">
```

- Grid 시스템(2차원) x, y축 을 동시에 조절 -> bootstrap이 grid system을 도입하면서 css가 급 발전하게 됨

  ```
  grid column = 12개 > 12는 약수가 많아서 구현할 수 있는 크기가 많음.
  
  <div class="container">			#container = 필수x 좌우측 보기 좋게하기 위함
    <div class="row>				#row = 필수o 
    
    
   <style>
      .square {
        width: 200px;
        height: 200px;
        background-color: wheat;
        border: 1px solid black;
        text-align: center;
        line-height: 200px;
      }
    </style>
  <div class="square col-1">1개당 12칸을 잡음 = 12덩이</div>
  <div class="square col-2">1개당 2칸을 잡음 = 6덩이</div>
  <div class="square col-3">1개당 3칸을 잡음 = 4덩이</div>
  <div class="square col-4">1개당 4칸을 잡음 = 3덩이</div>
  <div class="square col-6">1개당 6칸을 잡음 = 2덩이</div>
  <div class="square col-12">1개당 12칸을 잡음 = 1덩이</div>
  
  
  <div class="row">
   <div class="square col-2 offset-5">col-2 offset-5</div>
    </div>
     <!-- offset-숫자만큼 왼쪽에서 떨어져서 나타남 -->
    </div>
  ```

  

- Flex box(1차원) x, y축을 개별 조절,  Grid 시스템의 1차원 구현의 한계를 ''보완'' 

 