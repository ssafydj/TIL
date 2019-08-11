- CSS 기본 사용법

```css
h1{color:blue;font-size:15px;}

color, font-size = 프로퍼티
blue, 15px = 값

띄어쓰기x
; 으로 구분
: 으로 값 부여
- 으로 세부항목 접근
```

- 활용법

  ```html
  1. inline 
   > h1{color:blue;font-size:15px;}
  
  2. Embedding
  > <style>
      h1 {
          color: blue;
          font-size: 10px;
      }
  </style>
  
  3.link file(.css 파일만들어서 link로 연결)
  <link rel="stylesheet" href="00_intro.css">
  .css 파일에 
  h1 {
  color: blue;
  font-size: 10px;
  }
  형태로 작성
  ```

- 프로퍼티의 값

  ```html
  1. 키워드 = display, font, text, 
  
  2. 크기단위
  > px = 디바이스 마다 상대적
  > % = 디바이스 마다 상대적
  > em = 상속 또는 디폴트 사이즈에 따라 상대적
  > rem = 최상위 요소인 html을 기준으로 하므로 크기를 일정하게 조정가능
  > viewport = vw / vh = 디바이스 마다 스크린 크기가 달라 만들어짐
  
  3. 색상
  ```

- Box model

  ```html
  1. margin
  .margin {
  margin-top: 10px;
  margin-right: 20px:
  margin-bottom: 30px;
  margin-left: 40px;
  }
  
  2. padding
  .padding {
  padding-top: 10px;
  padding-right: 20px:
  padding-bottom: 30px;
  padding-left: 40px;
  }
  
  3. border
  .border {
  border-width: 2px;
  border-style: dashed;
  border-color: green;
  }
  
  4. shorthand
   4-1. margin shorthand
   .margin-1 {
  margin: 10px;					#상하좌우
  }
  
   .margin-2 {
  margin: 10px 20px;				#상하/좌우
  }
  
   .margin-3 {
  margin: 10px 20px 30px;			#상/좌우/하
  }
  
   .margin-4 {
  margin: 10px 20px 30px 40px;	#시계방향
  }
  
  4-2. border shorthand
   .border{
  border:2px dashed green;
  }
  ```

  

- Box-sizing

  ```
  content(default): content 를 기준으로 크기를 조절
  
  border: border를 기준으로 크기를 조절
  >padding이 늘어나도 일정 넓이까지는 화면이 깨지지 않는다.
  
  따라서 border box를 기본값으로 설정하고 시작해라!(style.css 양식으로 초기화)
  ```

  

- display 속성 (display: ____;)

  ```html
  1. block
  ex) div, h1~h6, p, ol, ul, li form...
  항상 새로운 라인에서 시작
  화면 크기 전체의 가로폭을 차지(width:100%)
  특정한 width 값을 설정하면, 나머지 부분은 margin 으로 처리
  
  margin-left: auto; = 오른쪽 정렬
  margin-right: auto; = 왼쪽 정렬(default)
  margin: 0 auto; = 가운데 정렬
  
  2. inline
  ex)span, a, img, button input...
  반드시 text가 필요하다 (content/text 너비만큼 width를 차지)
  새로운 라인에서 시작하지 않고, 문장의 중간에 들어갈 수 있다.
  width, height, margin 등 설정 못한다.
  상/하 여백은 line-height로 지정한다
  
  3. inline-block
  block과 inline의 특징을 모두 갖는다.
  inline 처럼 한 줄에 표시되면서(오른쪽 margin 사라짐) 
  block 처럼 width, height, margin 지정가능하다.
  
  4. None
  해당 요소를 화면에 표시하지 않고 심지어 공간조차 사라진다.
  
  5. visibility 속성
  visible = 해당 요소를 보이게 한다.(default)
  hidden = 해당 요소를 안보이게 한다.
  
   - display:none vs visibility:hidden 
   none은 공간조차 없이 사라지고, hidden은 사라지지만 공간은 유지된다.
  
  5-1. .opcaity {
  opacity: 0~1;   		#숫자가 낮을수록 흐려짐
  }
  ```

  

- Font 

  ```
  **google font 사용 tip
  <head>
  <link href="https://fonts.googleapis.com/css?family=Lexend+Exa|Nanum+Gothic|Roboto&display=swap" rel="stylesheet">
  
  <CSS>
  .google-font {
  font-family: 'Nanum Gothic', sans-serif;
  font-family: 'Roboto', sans-serif;
  font-family: 'Lexend Exa', sans-serif;
  font-size: 250%;
  }
  
  <html>
  <p class="google-font">세 시간 전 항구에서 출발한 배를 안개가 감쌌다.</p>
  
  **fontshorthand 
  font: font-style font-weight line-height font-size(필수) font-family(필수)  
  font: italic 2rem "Hack"
  ```

  

- Position

  ```
  1. position: static(기본위치)(default)
  위->아래(block), 왼쪽->오른쪽(inline) 으로 순서에 따라 배치
  부모 요소 내에 자식 요소로 있을 때는, 부모 요소의 위치를 기준으로 배치된다.
  
  2. position: relative(상대위치)
  static을 기준으로 top, bottom, left, right를 사용하여 위치를 이동시킨다.
  .relative {
  position: relative;
  top: 100px;
  bottom: 100px;
  }
  
  3. position: absolute(절대위치)
  static을 제외하고, position: relative; absolute; fixed; 로 선언된 부모 or 가장 가까이 있는 조상을 기준으로 top, bottom, left, right만큼 이동한다. 
  
  .parent {
  position: relative;
  }
  
  .absolute-child {
  position: absolute;
  top: 50px;
  left: 50px;
  }
  >.parent 를 기준으로 top: 50px left: 50px 이동한다. 
  
  a. 모든 부모가 static -> 부모인 position: static 위치를 기준으로 움직임
  b. 조상 중에 static이 아닌 가장 가까운 부모가 있을 때 -> 그 부모를 기준으로 움직임
  c. 자기의 부모나 조상이 움직이면 같은 거리 따라 움직인다.
  
  4. position: fixed(고정위치)
  부모 요소와 관계없이 브라우저의 viewport를 기준으로 위치를 이동시킨다.
  스크롤이 되더라도 화면에서 사라지지 않고 항상 같은 곳에 위치한다.
  .fixed {
  position:fixed;
  bottom:0;
  right:0;
  }
  ```

- float

  ```
  요소를 다음 요소 위에 떠 있게 한다.
  
  .float-left {
    float: left;
  }
  
  .float-right {
   float: right;
  }
  
  .clear {
   clear: left/right/both;
  }
  ```

  

- ol ul 태그 값 설정

  ```css
  html {						# rem 사용시 설정 필요
  font-size: 20px;
  }
  
  ol,
  ol li {
  	font-size: 1.2rem;
  }
  ```

  

- vw / vh 값 설정

  ```css
  .vw {
    font-size: 10vw;
  }
  
  .vh {
    font-size: 10vh;
  }
  ```

  

- 선택자 우선순위

  ```
  선택자 우선순위
  
  0. !importatnt
  1. 인라인 스타일
  2. 아이디 선택자 #
  3. 클래스 선택자 . 
  4. 태그선택자
  5. 전체선택자
  
  ** 가능하면 클래스 선택자만 사용하자!
  ```

  

- 그룹/자식/ 자손 선택자 (컴포넌트화 = 공통되는 부분은 하나로 묶고, 다른부분은 각각 따로 설정 )

```
그룹 선택자 = 모든 div에 같은 기본값을 줄 때 or 다른 태그에 같은 기본값을 줄 때

div {
  width: 100px;
  height: 100px;
  color: white;
  background-color: crimson;
  text-align: center;
  line-height: 100px;
}

**div 설정: text-align: center; & height = line-height -> text 수직 가운데 정렬
(단, text가 1 줄인 경우에만 가능)

p,
h3{
  color: grey;
}

자식 선택자 = 부모 ol의 후손인 li 셀렉터에 같은 값을 줄 때 -> 자식 셀렉터인 li에만 빨간색 10px가 적용됨 

ol > li {
color: red;
font-size: 10px;
}

자손 선택자 = 조상인 ul가 부모인 div 아래 자손 li에 값을 줄 때 
<ul>
  <div>
    <li>자손</li>
    <li>자손</li>
    <li>자손</li>
</div>
</ul>

*조상 선택자인 ul 중간에 공백을 두면 조상 선택자 이하에 (깊이에 상관없이) 모든 부모, 후손 셀렉터에 lime 색이 적용된다.
ul li {
color: lime;
}
```

- Background image 설정

  ```html
  <body>
    <div class="bg-box"></div>
  </body>
  
  .bg-box {
    height: 100%;
    background-image: url("images/someone\ who\ code.jpg");
    background-size: 600px 450px;
    background-size: contain;
    background-size: cover;
  
    /* background-repeat */
    background-repeat: no-repeat;
  
    /* background-position */
    background-position: 0, 0;
    background-position: center;
    background-attachment: fixed;
  
  
  - cover
  
  이미지의 크기 비율은 유지하면서, 부모 요소의 width, height 중 큰 값에 이미지를 맞춤.
  
  - contain
  
  배경이미지의 크기 비율을 유지하면서, 전체가 들어갈 수 있도록 이미지 크기를 조절한다.
  
  - attachment: fixed
  
  화면이 스크롤 되더라도 배경 이미지는 스크롤 되지않고 고정시킨다.
  
  **속 편하게 배경이미지 크기 맞추기
    background-position: center;
    background-attachment: fixed;
  ```

  

