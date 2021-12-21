# mysql 데이터베이스 관리!

<img width="916" alt="스크린샷 2021-12-21 오전 11 24 23" src="https://user-images.githubusercontent.com/89058117/146862476-5eecadaa-8648-4a58-b803-f1ed6ff9046d.png">

### DBeaver 에서 sql문 사용
<img width="1055" alt="스크린샷 2021-12-21 오후 3 43 17" src="https://user-images.githubusercontent.com/89058117/146883974-fb3215ac-ba71-4795-b3b5-e74479456f38.png">

```
-- 현재 접속한 db와 사용할 db가 다른 상태

use ML_DB

SELECT * FROM orderlist o 

select o.orderid '주문아이디', p.id as '주문물건번호'
FROM orderlist o
-- 두개 공통된것만 가져오겠다 
inner join product p 
on o.productid = p.id 

-- 어떤 회원이 어떤 물건을 얼마나 구매했는가? (회원id, 물건id, 총구매가격,주문id, 회원name)
SELECT m.id, o2.productid , o2.totalprice, o2.orderid, m.name 
FROM orderlist o2
inner join `member` m
on o2.memberid = m.id

-- park회원이 어떤 물건을 얼마나 구매했는가?
-- (주문id, 회원name, 물건id, 총구매가격)
-- 물건id 역순 정렬 
SELECT o2.orderid, m.name, o2.productid , o2.totalprice 
FROM orderlist o2
inner join `member` m
on o2.memberid = m.id and m.id = 'park'
order by productid desc




SELECT o2.orderid, m.name, o2.productid , o2.totalprice - 1000
FROM orderlist o2
inner join `member` m
on o2.memberid = m.id and m.id like 'a____' -- 언더바 4개
order by productid desc


-- apple의 갯수 세기 
SELECT COUNT(*) 
FROM orderlist o2
inner join `member` m
on o2.memberid = m.id and m.id = 'apple'


-- 멤버별 총 가
SELECT o3.memberid ,COUNT(*) , SUM(totalprice) 
FROM orderlist o3
inner join `member` m2
on o3.memberid = m2.id
GROUP BY m2.id



-- 개인별 몇개를, 최대 얼마만큼 구매했을까요? 
SELECT o3.memberid ,COUNT(*) , SUM(totalprice) 
FROM orderlist o3
inner join `member` m2
on o3.memberid = m2.id
GROUP BY m2.id



-- 물건별 몇 개를 얼마만큼 구매했을까요?
-- orderlist table에서 그룹별로 검
SELECT COUNT(*), SUM(totalprice)
FROM orderlist o5
GROUP BY o5.productid 


-- 물건별 몇 개를 얼마만큼 구매했고, 최대 구매금액은 얼마인가요? 
-- orderlist table에서 그룹별로 검
SELECT p.name ,sum(totalprice) , MAX(totalprice) 
FROM orderlist o3
inner join product p 
on o3.productid = p.id
GROUP BY p.id


-- 주문이 된 상품들 목록을 가지고 오고 싶을 때 
SELECT DISTINCT productid from orderlist o 

SELECT o6.productid , p6.name, COUNT(*) 
FROM orderlist o6
inner join product p6
on o6.productid = p6.id 
GROUP BY o6.productid 



-- member, board
-- 1) 개인별 게시판 글 작성수 
SELECT b.writer , COUNT(*) 
FROM board b
inner join `member` m 
on b.writer= m.id 
GROUP BY b.writer

-- 2) 개인별 게시판 글 작성수, 개인id, 개인name, 개인tel
SELECT b.writer , m.id, m.name, m.tel, COUNT(*) 
FROM board b
inner join `member` m 
on b.writer= m.id 
GROUP BY b.writer

-- 3) 게시판 제목, 내용, 작성자이름, 작성자tel
SELECT b.title , b.content ,b.writer , m.tel 
FROM board b 
inner join `member` m 
on b.writer= m.id 

-- 4) park이 작성한 글 작성수, 최근 게시물 번호
SELECT COUNT(*), MAX(b.id) 
FROM board b 
WHERE b.writer = 'park'

-- 5) apple이 작성한 글 중 java가 들어간 게시물 갯수
SELECT COUNT(*) 
FROM board b 
inner join `member` m 
on b.writer= m.id and b.writer = 'apple' and b.title = 'java' 

-- 6) park이 작성한 글 중 제일 오래된 게시물 번호, 제목, 내용
select b.writer, min(b.id)  , title, content 
from board b 
inner join `member` m 
on b.writer = m.id and m.id ='park' 

-- 7) 게시판 제목에 어떤 항목들이 올라왔나? (중복제거)
select distinct title
from board b 

-- 8) 게시판 내용 중 jsp가 들어간 글의 작성자이름과 작성자연락
select b.writer , m.tel
FROM board b 
inner join `member` m 
on b.writer = m.id and b.content like '%jsp%'



-- 서브쿼리 :  SQL 문을 실행하는 데 필요한 데이터를 추가로 조회하기 위해 SQL 문 내부에서 사용하는 SELECT 문을 의미합니다.
SELECT  * FROM product p 
WHERE p.id in(
	SELECT DISTINCT o.productid 
	from orderlist o 
	WHERE o.memberid = 'park'
)

SELECT DISTINCT o.productid 
from orderlist o 
WHERE o.memberid ='park'
```
