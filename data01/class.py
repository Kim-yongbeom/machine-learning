class Customer:
    def __init__(self, name, password, grade, bonus):
        self.name = name
        self.password = password
        self.grade = grade
        self.bonus = bonus
    def __str__(self):
        return self.name + self.password + self.grade + str(self.bonus)

a = Customer('admin', '1234', '관리자', 1000)
b = Customer('manager', 'pass', '준관리자', 1500)
c = Customer('sitemanager', 'sitepass', '준관리자', 1800)

print(a.name + '의 비밀번호는 ' + a.password +'입니다')
print(b.name + '는 '+ b.grade +'이고 ' + '마일리지는 ' + str(b.bonus) +'입니다')
avg = a.bonus+b.bonus+c.bonus
print('총 마일리지는 '+str(avg))
print('평균 마일리지는 '+str(avg//3))