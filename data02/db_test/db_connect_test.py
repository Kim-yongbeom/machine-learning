import pymysql

# db연결 connect()
conn = pymysql.connect(host='localhost', port=3306, user='root', password='gkdks120', db='cloth', charset='utf8')
# 모두 따옴표로 묶어주어 텍스트로 인자를 넘겨야 합니다.

curs = conn.cursor()
# 연결한 DB와 상호작용하기 위해 cursor 객체를 생성해주어야 합니다.
# 다양한 커서의 종류가 있지만,
# - 파이썬에서 데이터분석을 주로 pandas로 하고
# - RDBMS(Relational Darabase System)를 주로 사용하기 때문에
# 데이터 분석가에게 익숙한 데이터 프레임 형태로 결과를 쉽게 변환 할 수 있도록록#DictCursor 커서는 딕셔너리 형태로 결과를 반환해준다.
# DictCursor 가 아닌 일반 cursor를 사용하면 결과가 일반적으로 튜플형태로 리턴된다.

# 데이터 조작하기
# pymysql의 모든 데이터 조작은 execute()와 fetch()계열을 사용한다.
# 데이터 조회 - SELECT
id = 'abc'
sql = "select * from member1 where id='" + id + "'"
curs.execute(sql)
rows = curs.fetchall()
# select명령을 위해 sql문을 따로 변수에 넣어주고 cursor.execute(sql)을 사용해 sql를 실행합니다.
# 실행한 결과를 fetchall 을 이용해 받아온다.
# 메서드            설명
# fetchall()     모든 데이터를 한 번에 가져올 때 사용
# fetchone()     한 번 호출에 하나의 행만 가져올 때 사용
# fetchman(n)    n개만큼의 데이터를 가져올 때 사용
print("ID가 " + id + "인 회원정보 검색")

for x in rows:
   print(x)
conn.close()
