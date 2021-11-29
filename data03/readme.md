# mysql

### 트랜잭션(Transaction)은 데이터베이스의 완전성을 보장하기 위한 것입니다. 상태를 변화시키기 해서 수행하는 하나의 작업의 단위를 뜻합니다.

### root에서 유저설정

  - 유저 생성
    - create user 원하는이름@localhost identified by '원하는비밀번호!';
    - 만든 아이디로 접속하려면 mysql -u 원하는이름 -p

  - 보안설정
    - grant all privileges on  *.* to '설정한이름'@'localhost';

### 데이터 베이스 만들기
- create database 원하는이름

### 테이블 만들기
- create table 원하는이름 ( id varchar(100), pw varchar(100), name varchar(100), tel varchar(100));

### 테이블 row생성
- insert into 테이블명 values ('200','200','200','200');

### 테이블 row삭제
- DELETE FROM plan WHERE 컬럼명=100;

### 테이블 row확인
- select * from 테이블명;

### 자동 커밋확인하기
- select @@autocommit;

### 수동 커밋
- set @@autocommit = 0; 
- commit;

### 행 추가 취소 (마지막 커밋 이후)
- rollback;
