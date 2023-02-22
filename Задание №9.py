from tkinter import *
from random import randint
def gen():
    canvas.delete('all')
    f=randint(1,3)
    if f==1:
        x1,y1,z=randint(1,x),randint(1,y),100
        if x1+z<=x:
            if y1+z<=y:
                canvas.create_oval(x1,y1,x1+z,y1+z,fill='black')
            else:
                canvas.create_oval(x1,y1,x1+z,y1-z,fill='black')
        else:
            if y1+z<=y:
                canvas.create_oval(x1,y1,x1-z,y1+z,fill='black')
            else:
                canvas.create_oval(x1,y1,x1-z,y1-z,fill='black')
    if f==2:
        x1,y1,z=randint(1,x),randint(1,y),100
        if x1+z<=x:
            if y1+z<=y:
                canvas.create_rectangle(x1,y1,x1+z,y1+z,fill='black')
            else:
                canvas.create_rectangle(x1,y1,x1+z,y1-z,fill='black')
        else:
            if y1+z<=y:
                canvas.create_rectangle(x1,y1,x1-z,y1+z,fill='black')
            else:
                canvas.create_rectangle(x1,y1,x1-z,y1-z,fill='black')
    if f==3:
        canvas.create_polygon(randint(1,x),randint(1,y),randint(1,x),randint(1,y),randint(1,x),randint(1,y),)
root=Tk()
x,y=810,500
canvas=Canvas(width=x,height=y,bg='white')
canvas.pack()
button=Button(text='Создать фигуру',command=gen).pack()
root.mainloop()
