from tkinter import *
import db_test.dao as dao

def create():
    # dao를 import 해서 써보세요
    vo = [id_text.get(), pw_text.get(), name_text.get(), tel_text.get()]
    # print(id_text.get())
    dao.create(vo)

def delete():
    pass


w = Tk()
w.geometry('500x800')
w.config(bg='lightgray')

icon = PhotoImage(file='car.png')
dogLabel = Label(w, image=icon)
dogLabel.pack()

id_label = Label(w, text='아이디입력', font=('맑은 고딕', 20), bg='lightgray', fg='blue')
id_label.pack()

id_text = Entry(w, font=('맑은 고딕', 20), bg='yellow', fg='red')
id_text.pack()

pw_label = Label(w, text='패스워드입력', font=('맑은 고딕', 20), bg='lightgray', fg='blue')
pw_label.pack()

pw_text = Entry(w, font=('맑은 고딕', 20), bg='yellow', fg='red')
pw_text.pack()

name_label = Label(w, text='이름입력', font=('맑은 고딕', 20), bg='lightgray', fg='blue')
name_label.pack()

name_text = Entry(w, font=('맑은 고딕', 20), bg='yellow', fg='red')
name_text.pack()

tel_label = Label(w, text='전화번호입력', font=('맑은 고딕', 20), bg='lightgray', fg='blue')
tel_label.pack()

tel_text = Entry(w, font=('맑은 고딕', 20), bg='yellow', fg='red')
tel_text.pack()

button = Button(w, width=30, height=3, bg='green', font=('맑은 고딕', 10), text='회원가입', command=create)
button.pack()

button2 = Button(w, width=30, height=3, bg='green', font=('맑은 고딕', 10), text='회원탈퇴', command=delete)
button2.pack()

w.mainloop()