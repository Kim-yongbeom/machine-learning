import db_test.dao as dao

rows = dao.all()

for i in range(0, len(rows)):
    print(rows[i])

for row in rows:
    print('결과는' + row[0] + " " + row[1] + " " + row[2] + " " + row[3])