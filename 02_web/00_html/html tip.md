- 단어에 hyper  link 설정

  ```html
  <h2><a href="https://docs.python.org/ko/3/tutorial/index.html">파이썬</a></h2>
  
  <h2><a href="https://docs.python.org/ko/3/tutorial/index.html" target="_blank" id="python">파이썬</a></h2>
  
  >파이썬</a></h2> = 닫는 태그는 가장 뒤에 위치
  target="blank" = 새 tap에서 열기 
  id="python" = "python" 이라는 id로 링크에 접근
  ```

- 이미지에 hyper link 설정

  ```html
  <a href="#python"><img src="images/python-7be70baaac.png" alt="python image" width="50px" height="50px"></a>
  
  <a href="#python"> = 위에서 설정한 id 값을 활용(다시 url 나열할 필요없다)
  <img src="images/파일명"> = imgages 폴더 안에 이미지 보관
  alt="python" = 스크린 리더 또는 이미지 파일이 로딩되지 않을 때 대체할 내용
  width="50px" height="50px" = 이미지 크기 설정
  ```

- table 행/열 설정

  ```html
  <table border="1px solid black" summary="#">    # table선 표시
      <caption>제목</caption>				  	   # table 제목
      <thead>										
        <tr>										# table row 가로열(행)	
          <th></th>								
          <th>월</th>							#table head(열) (bold 처리)
          <th>화</th>									=td=table data
          <th>수</th>
        </tr>
      </thead>
  </table>
      
  <thead></thead>
  <tbody></tbody>
  <tfoot></tfoot>
  으로 semantic tag 부여
   
  colspan = 열의 갯수 조정(좌우로 넓게) > 다음 열의 행 1개 삭제 필요
  rowspan = 행의 갯수 조정(상하로 길게) > 다음 행의 열 1개 삭제 필요
  ```


- stlye 사용법

  ```html
  <li style="list-stype-type: none"></li>
  ```

  