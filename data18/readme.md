# 정규화

### 추천시스템
![화면 캡처 2021-12-20 101329](https://user-images.githubusercontent.com/89058117/146698509-2b4fb5c8-333a-403a-b7da-c07b23668026.png)


![캡처](https://user-images.githubusercontent.com/89058117/146698511-44013f86-68f9-4ca0-9609-13ddaa06471f.PNG)

### SQL
- DDL (Data Definition Language)
  - db생성/수정/삭제, table 생성/수정/삭제
  - create, alter, drop
- DML (Data Manipulation Languagem)
  - CRUD
  - insert, select, update, delete
- DCL (Data Control Language)
  - 계정관리, 백업/복구

### 정규화가 왜 필요한가
- 이상현상이 발생

### 정규화하지 않으면 나타나는 현상
- 이상현상

### 언제 이상현상이 발생하는가?
- 삽입이상, 갱신이상, 삭제이상

### 이상현상이 왜 나타나는가?
- 중복

### 이상현상을 해결하는 방법은?
- 분할

### 분할해 나가는 과정은?
- 정규화 과정

### 정규화순서
- 제 1정규화(원자값) -> 제 2정규화(완전종속(부분종속)) -> 제 3정규화(이행종속x)

### 데이터를 추출할 때
- 분할해 놓은 테이블들을 join해서 가지고 와야함
- on join시 기준이 되는 컬럼을 지정
- 기준에 해당하는 값들이 양쪽 테이블에 있는 경우 : inner join
- 기준에 해당하는 값이 없는 경우 : outer join
