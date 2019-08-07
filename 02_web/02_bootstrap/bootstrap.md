### position



1. static(기본위치): 부모 위치를 기준으로 움직인다.

2. **relative위치: 자신의 과거 위치인 기본위치를 기준으로 좌표 property를 사용하여 상하좌우로 이동 

   ex) top 10px = 아래로 10px 이동

3. **absolute 위치: 부모 요소 또는 가장 가까운 조상요소를 기준으로 좌표 property만큼 이동

   즉, relative absolute fixed 프로퍼티가 선언되어 있는 부모 또는 조상 요소를 기준으로 위치가 결정된다. 

4. fixed 고정 위치: 부모 요소와 관계없이 ''브라우저의 viewport를 기준''으로 좌표 프로퍼티를 사용하여 이동한다.

   스크롤이 되어도 화면에서 사라지지 않고 <u>항상 같은 곳에 위치</u>한다.





### Bootstrap (front-end framework / library)

<>bootstrap을 주로 사용하지만, CSS를 보완적으로 사용함.

HTML vs BOOTstrap > 깔끔하고 세련됨

```html
설치: bootstrap > documentation> download css js 복붙
```

```html
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
```

```html
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
```



CDN: 별도의 파일을 다운로드 할 필요없이  link를 통해 데이터를 쉽고, 빠르고, 데이터 소모없이 사용하게함.

(=적절한 수준의 캐시설정으로 빠르게 로딩할 수 있다.) content delivery network



* ''*<u>클래스</u>'' *로 동작한다.  
* <u>이미 bootstrap에 만들어진 class name 을 자유롭게 활용하면 된다.</u>

```
**margin
margin:0;   .m-0  상하좌우0

margin-right:0    .mr-0 우0

margin-left/right:  .mx-0 좌우(x축)0

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

```
##color
.bg-primary
.bg-secondary
.bg-success
.bg-danger
.bg-warning
.bg-info
.bg-light
.bg-dark
.bg-white

###color 활용법
.text-success -> 초록색 text
.alert-warning -> 노랑색 alert
.btn-secondary -> 회색 button
.navbar-dark.bg-primary -> 2개 이상 .으로 연결해서 사용가능
.border-success -> 초록색 border

##display
.d-block
.d-inline
.d-inline-block

##position
.position-static
.position-relative
.position-absolute
.position-fixed

```

- Grid 시스템(2차원) x, y축 을 동시에 조절 -> bootstrap이 grid system을 도입하면서 css가 급 발전하게 됨

- Flex box(1차원) x, y축을 개별 조절,  Grid 시스템의 1차원 구현의 한계를 ''보완'' 

 