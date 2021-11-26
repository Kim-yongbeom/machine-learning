import db_test.dao as dao

id = input('id >> ')
pw = input('pw >> ')
tel = input('tel >> ')

# 값을 보낼때 두가지 방법
# 값을 전달할 때 묶어서 보내는 역할의 클래스(data transfer object, DTO, value Object, VO)
# list
vo = list()
vo.append(pw)
vo.append(tel)
vo.append(id)
# db_test.dao.create(vo)
dao.update(vo)