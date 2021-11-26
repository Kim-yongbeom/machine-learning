import db_diary.diary as diary

id = input('검색할 id >> ')


# 값을 보낼때 두가지 방법
# 값을 전달할 때 묶어서 보내는 역할의 클래스(data transfer object, DTO, value Object, VO)
# list


# db_test.dao.create(vo)
diary.read(id)

# 모듈을 만들 때는 각자의 역할에 충실하도록, 역할을 섞어서 만들면안된다.
# 응집도