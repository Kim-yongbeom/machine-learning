from tkinter import *
import db_diary.diary as diary

def create():
    vo = [writeday_text.get(), title_text.get(), content_text.get()]
    diary.create(vo)

def delete():
    pass


w = Tk()
w.geometry('500x800')
w.config(bg='lightgray')

icon = PhotoImage(file='car.png')
dogLabel = Label(w, image=icon)
dogLabel.pack()

writeday_label = Label(w, text='작성일자', font=('맑은 고딕', 20), bg='lightgray', fg='blue')
writeday_label.pack()

writeday_text = Entry(w, font=('맑은 고딕', 20), bg='yellow', fg='red')
writeday_text.pack()

title_label = Label(w, text='제목', font=('맑은 고딕', 20), bg='lightgray', fg='blue')
title_label.pack()

title_text = Entry(w, font=('맑은 고딕', 20), bg='yellow', fg='red')
title_text.pack()

content_label = Label(w, text='댓글', font=('맑은 고딕', 20), bg='lightgray', fg='blue')
content_label.pack()

content_text = Entry(w, font=('맑은 고딕', 20), bg='yellow', fg='red')
content_text.pack()

button = Button(w, width=30, height=3, bg='green', font=('맑은 고딕', 10), text='회원가입', command=create)
button.pack()

button2 = Button(w, width=30, height=3, bg='green', font=('맑은 고딕', 10), text='회원탈퇴', command=delete)
button2.pack()

w.mainloop()