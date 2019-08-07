### position



1. static(기본위치): 부모 위치를 기준으로 움직인다.

2. **relative위치: 자신의 과거 위치인 기본위치를 기준으로 좌표 property를 사용하여 상하좌우로 이동 

   ex) top 10px = 아래로 10px 이동

3. **absolute 위치: 부모 요소 또는 가장 가까운 조상요소를 기준으로 좌표 property만큼 이동

   즉, relative absolute fixed 프로퍼티가 선언되어 있는 부모 또는 조상 요소를 기준으로 위치가 결정된다. 

4. fixed 고정 위치: 부모 요소와 관계없이 브라우저의 viewport를 기준으로 좌표 프로퍼티를 사용하여 이동한다.

   스크롤이 되어도 화면에서 사라지지 않고 항상 같은 곳에 위치한다.





### Bootstrap (front-end framework / library)

HTML vs BOOTstrap > 깔끔하고 세련됨

```html
설치: bootstrap > documentation> css js 복붙

reboot(초기화) 
```

CDN: 다운로드 할 필요없이  link로 데이터를 쉽게, 빠르게, 데이터 소모없이 사용가능.

(적절한 수준의 캐시설정으로 빠르게 로딩할 수 있다.) content delivery network



* ''*<u>클래스</u>'' 위주*로 작동한다.  이미 bootstrap에 만들어놓은  form 을 class 몇 개만 추가해서 자유롭게 적용하여 사용하면 된다.

```
.m-0 상하좌우 0

.mr-0 우 0

.mx-0 좌우 0

.py-0 패딩 상하 0

.mt-1 0.25rem

.mt-2 4px = 

.mt-3 16px

.mt-4 

.mx-auto (좌우를 이동) = 가운데 정렬

etc...
```

```
.bg-primary
.text / padding-success
.btn (button)
.navbar-dak.bg-primary
```

- Grid 시스템(2차원) x, y축 을 동시에 조절 -> bootstrap이 grid system을 도입하면서 css가 급 발전하게 됨

- Flex box(1차원) x, y축을 개별 조절,  Grid 시스템의 1차원 구현의 한계를 ''보완'' 

 