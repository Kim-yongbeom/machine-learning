# mysql

### 새로운 아이디 만들기
- grant all privileges on  *.* to 'apple'@'%' indentified by '원하는 비밀번호';
- 만든 아이디로 접속하려면 mysql -u apple -p

### 테이블 만들기
- create table member ( id varchar(100), pw varchar(100), name varchar(100), tel varchar(100));

### 자동 커밋확인하기
- select @@autocommit;
- 바꾸고 싶다면 set @@autocommit = 0;

