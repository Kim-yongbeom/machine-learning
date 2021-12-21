# mysql 데이터베이스 관리

<img width="916" alt="스크린샷 2021-12-21 오전 11 24 23" src="https://user-images.githubusercontent.com/89058117/146862476-5eecadaa-8648-4a58-b803-f1ed6ff9046d.png">
<br/>
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
```
<br/>
<img width="469" alt="스크린샷 2021-12-21 오전 11 24 49" src="https://user-images.githubusercontent.com/89058117/146862483-215d28fd-3d40-4b2c-80c1-dc689ba291d6.png">
<br/>
<img width="582" alt="스크린샷 2021-12-21 오전 11 38 15" src="https://user-images.githubusercontent.com/89058117/146862487-7c39b52a-37f6-4a83-bf52-46c90bdb2cd2.png">
<br/>
<img width="472" alt="스크린샷 2021-12-21 오전 11 41 35" src="https://user-images.githubusercontent.com/89058117/146862488-72bca674-043e-41b7-8bb3-f4b61981f57b.png">
<br/>
<img width="523" alt="스크린샷 2021-12-21 오전 11 47 40" src="https://user-images.githubusercontent.com/89058117/146862492-21df026a-6756-4493-9350-51dc8c08bdc1.png">
<br/>
<img width="540" alt="스크린샷 2021-12-21 오전 11 47 50" src="https://user-images.githubusercontent.com/89058117/146862494-67d7c1ed-8d86-4007-8c70-a664283eb8be.png">
<br/>
<img width="539" alt="스크린샷 2021-12-21 오전 11 48 48" src="https://user-images.githubusercontent.com/89058117/146862496-ad2c9add-2b27-4d22-9cd1-c60b7f14251b.png">
<br/>
<img width="339" alt="스크린샷 2021-12-21 오전 11 52 52" src="https://user-images.githubusercontent.com/89058117/146862884-d90a7b48-86a5-4711-8cb0-4829488bc24f.png">
<br/>
<img width="441" alt="스크린샷 2021-12-21 오후 12 09 54" src="https://user-images.githubusercontent.com/89058117/146866587-03a27176-8f7b-4b86-b697-4d036b41900d.png">
<br/>
<img width="460" alt="스크린샷 2021-12-21 오후 12 12 12" src="https://user-images.githubusercontent.com/89058117/146866588-b1e4676d-cc91-4915-8058-649c3aeea87e.png">
<br/>
<img width="397" alt="스크린샷 2021-12-21 오후 12 30 11" src="https://user-images.githubusercontent.com/89058117/146866590-4a1a125a-7e25-4ff1-b3dc-2dc7bfa46d9c.png">
<br/>
<img width="446" alt="스크린샷 2021-12-21 오후 12 34 07" src="https://user-images.githubusercontent.com/89058117/146866591-1d5aab86-96a4-44d6-8a27-c7ddb65a4ebe.png">
<br/>
<img width="401" alt="스크린샷 2021-12-21 오후 12 40 19" src="https://user-images.githubusercontent.com/89058117/146874040-e03c1f51-b34d-433f-8c00-8fb26d83ca01.png">
<br/>
<img width="490" alt="스크린샷 2021-12-21 오후 3 07 34" src="https://user-images.githubusercontent.com/89058117/146880097-24592771-bd11-4611-9506-c20ad21285cc.png">
