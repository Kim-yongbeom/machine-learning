import pymysql

class DIARY():

    def create(vo):
        conn = pymysql.connect(host='localhost',
                        port=3306,
                        user='root',
                        password='gkdks120',
                        db='cloth',
                        charset='utf8') #파이썬 default 문법
        print('1. db연결 성공', conn)

        cur = conn.cursor()
        print('2. db연결 스트림을 접근할 수 있는 객체 획득 성공', cur)

        sql = 'insert into diary values(null,%s,%s,%s)'
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

        # id값에 해당하는 row 가져옴
        rows = cur.fetchall()
        print(len(rows))
        print('3. sql문을 만들어서 mysql로 보낸다.', result)
        conn.commit()
        conn.close()
        return rows

# 해당 모듈이 main되어서 실행될 때만, 실행해 주는 부분
if __name__ == '__main__':
    diary = DIARY()
    diary.create("bar","bar","bar","bar")