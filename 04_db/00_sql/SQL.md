`.`:sqlite3 프로그램의 기능을 실행하는것

`;`:세미콜론 까지가 하나의 명령(Query)으로 간주

실행 및 종료: sqlite3 tutorial.sqlite3 <>ctrl z



- SQL 문법은 소문자로 작성해도 기능하지만, 대문자를 권장한다
- 하나의 DB에는 여러개의 table 이 존재한다.



### CREATE(생성)

```
CREATE TABLE classmates (
id INT PRIMARY KEY,
name TEXT 
age INT,
address TEXT
);
```

테이블 목록 조회: .tables

전체 스키마 조회: .schema



### DROP(삭제)

```
DROP TABLE classmates;
```



### INSERT(추가)

SELECT * FROM classmates;

> tables 전체 조회

```
INSERT INTO table(column1, column2, .....)
	VALUES(value1, value2, ......);
	
(단, 모든열에 데이터를 넣을 때에는 COLUMN을 명시할 필요가 없다)
 
INSERT INTO classmates (name, age) VALUES ('홍길동', 23); 으로 사용가능
```

```
INSERT INTO classmates VALUES (2, '홍길동', 30, '서울');
```



### SELECT(불러오기)

```
SELECT column1, column2 FROM table

>> SELECT id, name FROM classmates;
```



SELECT rowid, * FROM classmates;

> 따로 PK 속성을 설정하지 않으면 1부터 자동으로  증가하는 PK 옵션을 가진 rowid 컬럼을 정의함

> id `INTEGER PRIMARY KEY`: 를 설정하지 않으면, rowid가 자동으로 설정됨

 

SELECT rowid, name FROM classmates;

> 테이블의 값을 모두 불러오기



SELECT rowid, name FROM classmates LIMIT 1;

> 첫 데이터부터 특정 갯수의 데이터만 불러오기



SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;

> 특정 위치(OFFSET) 이후로 부터 몇개의 데이터(LIMIT)를 가져옴



SELECT rowid, name FROM classmates WHERE address='서울';

> classsmates 테이블에서 주소가 서울인 데이터만 출력



 SELECT DISTINCT age FROM classmates;

> 중복없이 age 값을 출력



### DELETE(삭제)

DELETE FROM classmates WHERE rowid=4;

> rowid=4인 컬럼을 삭제 
>
> DELETE를 사용할 때는 중복이 불가능한 unique 값인 id를 기준으로 사용하자.

-----------------------------

### AUTOINCREMENT

삭제된 id 값은 pass하고 재사용되지 않도록 하는 기능 or 삭제된 id 값을 매꾸면서 사용되므로



rowid 의 최대값은 64비트 8바이트 실수의 최대값

== 922경

INSERT INTO 를 한다면,

1. AUTOINCREMENT 가 없을 때: 중간에 없는 ID 를 재사용하므로 에러가 나지 않을 것.
2. AUTOINCREMENT 가 있을 때: 최대 레코드를 넘어서기 때문에 에러가 발생.



### UPDATE(수정)

```
UPDATE table
SET column1=value1, column2=value2,...
WHERE condition
```

```
classmates 테이블에서 id=3인 레코드를 홍길동, 제주도로 수정해봅시다.

sqlite> UPDATE classmates
   ...> SET name='홍길동', address='제주도'
   ...> WHERE rowid=3;
sqlite> SELECT rowid, * FROM classmates;
```



## USERS.csv 파일

```
.mode csv
.import users.csv users 
(새로운 csv 파일 불러오기)
```

```
특정 tabled 에서 특정 조건의 column만 가져오기

SELECT * FROM table
Where condition
```

SELECT * FROM users WHERE age >= 30;

> users에서 age가 30 이상인 사람만 가져오기

SELECT first_name FROM users WHERE age >= 30;

> users에서 age가 30 이상인 사람의 이름 가져오기

SELECT last_name, age FROM users WHERE age >= 30 and last_name ='김';

> users에서 age가 30 이상이고 성이 김인 사람의 성과 나이를 가져오기



p81~

다음의 표현식은 기본적으로 숫자일때만 가능하다

- AVG(column)
- SUM()
- MIN()
- MAX()

```
sqlite> SELECT COUNT(*) FROM users;
1000
sqlite> SELECT AVG(age) FROM users WHERE age >=30;
35.1763285024155
```

```
sqlite> SELECT first_name, MAX(balance) FROM users;
선영|990000
```

```
sqlite> SELECT AVG(balance) FROM users WHERE age >= 30;
153541.425120773
```

### LIKE(와일드카드)

`-`: 반드시 이 자리에 한 개으 ㅣ문자가 존재햐아 하낟

`%` : 이 자리에 문자열이 있을수도 없어도 괜찮



`2_3_%` / `2_%3_%` 

SELECT * FROM users WHERE age LIKE '2%';

> 20대인 사람들의 목록 불러오기

sqlite> SELECT * FROM users WHERE PHONE LIKE '02-%';

> 지역번호가 02인 사람들 불러오기

sqlite> SELECT * FROM users WHERE first_name LIKE '%준';

> 이름이 준으로 끝나는 사람들 불러오기

sqlite> SELECT * FROM users WHERE phone LIKE '%-5114-%';

> 전화번호 가운데가 5114 인 사람 불러오기



### 정렬

SELECT columns FROM table ORDER BY column1, column2[ASC/DESC]



sqlite> SELECT * FROM users ORDER BY age ASC LIMIT 10;

> 오름차순 나이순으로 10개 뽑기

sqlite> SELECT * FROM users ORDER BY age, last_name ASC LIMIT 10;

> 성과 이름을 기준으로 오름차순 10개 뽑기

sqlite> SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10;

> 내림차순으로 상위 10개 성과 이름 뽑기



### ALTER

1. table 이름 변경 

   >  ALTER TABLE exist_table RENAME TO new_table;

2. 특정 테이블에 새로운 컬럼 추가

   > ALTER TABLE table ADD COLUMN co_name DATATYPE;

   - Error: Cannot add a NOT NULL column with default value NULL 오류 발생

     - 해결책 1. ALTER TABLE news ADD COLUMN created_at DATETIME (NOT NULL);

       > not null 조건을 제거

     - 해결책 2. INSERT INTO news values('title', 'content', datetime('now', 'localtime'));

       > not null 을 유지해야한다면 새로운 default 값을 설정

     sqlite> `SELECT * FROM news;` 로 테이블 구성 확인

