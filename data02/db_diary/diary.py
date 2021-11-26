import pymysql

def create(vo):
    conn = pymysql.connect(host='localhost',
                    port=3306,
                    user='root',
                    password='gkdks120',
                    db='cloth',
                    charset='utf8') #파이썬 default 문법
    print('1. db연결 성공', conn)


    # DB 접속이 성공하면, Connection 객체로부터
    # cursor() 메서드를 호출하여 Cursor 객체를 가져온다.
    # DB 커서는 Fetch 동작을 관리하는데 사용되는데, 만약 DB 자체가 커서를 지원하지 않으면,
    # Python DB API에서 이 커서 동작을 Emulation 하게 된다.
    cur = conn.cursor()
    print('2. db연결 스트림을 접근할 수 있는 객체 획득 성공', cur)

    # id가 자동증가이기 때문에 null을 넣어줘서 id값을 받지않는다.
    sql = 'insert into diary values(null,%s,%s,%s)'

    # Cursor 객체의 execute() 메서드를 사용하여 SQL 문장을 DB 서버에 보낸다.
    result = cur.execute(sql, vo)
    print('3. sql문을 만들어서 mysql로 보낸다.', result)

    conn.commit()
    conn.close()

def update(vo):
    conn = pymysql.connect(host='localhost',
                    port=3306,
                    user='root',
                    password='gkdks120',
                    db='cloth',
                    charset='utf8') #파이썬 default 문법
    print('1. db연결 성공', conn)

    cur = conn.cursor()
    print('2. db연결 스트림을 접근할 수 있는 객체 획득 성공', cur)

    # sql = "insert into member values ('" + id + "', '" + pw + "', '" + name + "', '" + tel + "')"
    # sql = "insert into member values ('" + vo[0] + "', '" + vo[1] + "', '" + vo[2] + "', '" + vo[3] + "')"
    sql = 'update diary set title = %s, content = %s where id = %s'

    result = cur.execute(sql, vo)
    print('3. sql문을 만들어서 mysql로 보낸다.', result)

    conn.commit()
    conn.close()

def delete(vo):
    conn = pymysql.connect(host='localhost',
                    port=3306,
                    user='root',
                    password='gkdks120',
                    db='cloth',
                    charset='utf8') #파이썬 default 문법
    print('1. db연결 성공', conn)

    cur = conn.cursor()
    print('2. db연결 스트림을 접근할 수 있는 객체 획득 성공', cur)

    # sql = "insert into member values ('" + id + "', '" + pw + "', '" + name + "', '" + tel + "')"
    # sql = "insert into member values ('" + vo[0] + "', '" + vo[1] + "', '" + vo[2] + "', '" + vo[3] + "')"
    sql = 'delete from diary where id = %s'

    result = cur.execute(sql,vo)
    print('3. sql문을 만들어서 mysql로 보낸다.', result)

    conn.commit()
    conn.close()

def read(id):
    conn = pymysql.connect(host='localhost',
                    port=3306,
                    user='root',
                    password='gkdks120',
                    db='cloth',
                    charset='utf8') #파이썬 default 문법
    print('1. db연결 성공', conn)

    cur = conn.cursor()
    print('2. db연결 스트림을 접근할 수 있는 객체 획득 성공', cur)

    # sql = "insert into member values ('" + id + "', '" + pw + "', '" + name + "', '" + tel + "')"
    # sql = "insert into member values ('" + vo[0] + "', '" + vo[1] + "', '" + vo[2] + "', '" + vo[3] + "')"
    sql = 'select * from diary where id = %s'
    result = cur.execute(sql, id)

    # id값에 해당하는 row 가져옴
    row = cur.fetchone()
    print(row)
    print('3. sql문을 만들어서 mysql로 보낸다.', result)
    conn.commit()
    conn.close()
    return row

def all():
    conn = pymysql.connect(host='localhost',
                    port=3306,
                    user='root',
                    password='gkdks120',
                    db='cloth',
                    charset='utf8') #파이썬 default 문법
    print('1. db연결 성공', conn)

    cur = conn.cursor()
    print('2. db연결 스트림을 접근할 수 있는 객체 획득 성공', cur)

    # sql = "insert into member values ('" + id + "', '" + pw + "', '" + name + "', '" + tel + "')"
    # sql = "insert into member values ('" + vo[0] + "', '" + vo[1] + "', '" + vo[2] + "', '" + vo[3] + "')"
    sql = 'select * from diary'
    result = cur.execute(sql)

    # 전부 가져옴
    rows = cur.fetchall()
    print(len(rows))
    print('3. sql문을 만들어서 mysql로 보낸다.', result)
    conn.commit()
    conn.close()
    return rows

# 해당 모듈이 main되어서 실행될 때만, 실행해 주는 부분
if __name__ == '__main__':
    create("bar","bar","bar","bar")