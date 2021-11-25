# 1
id = 'root'
name = '홍길동'
print('아이디가 %s인 %s님이 로그인되었습니다.' %(id,name))

# 2
num1 = 33
num2 = 7
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1//num2)
print(num1%num2)

# 3
age = int(input('현재 나이를 입력하세요 : '))
print('%s님의 10년 후의 나이는 %d세 입니다.\n' %(name, age+10))

# 4
money = int(input('용돈 : '))
if money >= 10000:
    print('엄마 너무 용돈이 많아요\n')
else:
    print('엄마 너무 용돈이 적어요\n')

# 5
num = int(input('숫자를 입력하세요 : '))
if num % 2 == 1:
    print('홀수입니다\n')
else:
    print('짝수입니다\n')

# 6
score = int(input('실적을 입력하세요 : '))
if score >= 1000:
    bonus = score*0.2
    print('축하합니다. 실적을 달성하셨습니다!')
    print('당신의 이번달 보너스는 %d만원 입니다.'%bonus)
else:
    print('실적을 달성하지 못했습니다.')

