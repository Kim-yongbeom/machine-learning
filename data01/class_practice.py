class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
    def run(self):
        speed_result = self.speed
        print(speed_result)
    def start(self):
        color_result = self.color
        print(color_result)

class Truck (Car):
    def load(self):
        print('load!!!')

a = Car('빨간색',80)
b = a.run()
c = a.start()

d = Truck('초록색', 70)
e = d.load()
f = d.start()
g = d.run()

######################################################################
class Phone:
    # 부품(객체 object)을 만들기위해서는 틀이 필요.
    # 틀이 class
    # 전화기만의 공통적인 성질로 틀을 만들어야 한다.

    # 공통적인 성질: 특성, 속성(property, attribute) => 멤버변수
    color = None
    ram = 0
    # 객체생성시 자동호출되는 함수 : 생성자 함수
    def __init__(self, c, r):
        self.color = c
        self.ram = r

    # 공통적인 동작: 기능(function) => 멤버함수
    def call(self):
        print('전화하다.')

    def game(self):
        print('게임하다.')

    # 주소대신에 주소가 가르키고 있는 멤버변수의 값을 프린트
    # 이거 빼면 주소 나옴
    def __str__(self):
        return self.color + ' ' + str(self.ram)

myPhone = Phone('red',256) # 객체 생성
yourPhone = Phone('blue',128)

print(myPhone)
print(yourPhone)

# 클래스안에 __init__ 생성자 함수와 같다
# myPhone.color = 'red'
# print(myPhone.color)
# yourPhone.color = 'blue'
# print(yourPhone.color)