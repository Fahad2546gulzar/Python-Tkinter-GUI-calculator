from tkinter import *
root=Tk()
root.title("Calculator")
root.background="gray"
root.geometry('2800x2500')
Label(root,text="Calculator",fg="purple",font=('Calibri',40)).place(x=491,y=10)
e=Entry(root,width=80,borderwidth=4,font=100)
e.place(x=185,y=100)
#root.geometry('2800x2500')
def bc(num):
    cu=e.get()
    e.delete(0,END)
    e.insert(0,str(cu)+str(num))
    global n
    n=cu
def clear():
    e.delete(0,END)
def ba():
    e.insert(END,"+")
def mi():
    e.insert(END,"-")
def mu():
    e.insert(END,"*")
def di():
    e.insert(END,"/")
def eq():
   eva= eval(e.get())
   e.delete(0,END)
   e.insert(0,eva)
def po():
    e.insert(END,".")
import math
def si():
    getv=e.get()
    e.delete(0,END)
    e.insert(0, math.tan(int(getv)))
def cos():
    getv=e.get()
    e.delete(0,END)
    e.insert(0,math.cos(int(getv)))
def tan():
    getv=e.get()
    e.delete(0,END)
    e.insert(0,math.tan(int(getv)))
button_1=Button(root,text="1",padx=40,pady=20,bg='yellow',fg='blue',command=lambda:bc(1))
button_4=Button(root,text="4",padx=40,pady=20,bg='yellow',fg='blue',command=lambda:bc(4))
button_7=Button(root,text="7",padx=40,pady=20,bg='yellow',fg='blue',command=lambda:bc(7))
button_2=Button(root,text="2",padx=40,pady=20,bg='yellow',fg='blue',command=lambda:bc(2))
button_3=Button(root,text="3",padx=40,pady=20,bg='yellow',fg='blue',command=lambda:bc(3))

button_5=Button(root,text="5",padx=40,pady=20,bg='yellow',fg='blue',command=lambda:bc(5))
button_6=Button(root,text="6",padx=40,pady=20,bg='yellow',fg='blue',command=lambda:bc(6))
button_7=Button(root,text="7",padx=40,pady=20,bg='yellow',fg='blue',command=lambda:bc(7))
button_8=Button(root,text="8",padx=40,pady=20,bg='yellow',fg='blue',command=lambda:bc(8))
button_9=Button(root,text="9",padx=40,pady=20,bg='yellow',fg='blue',command=lambda:bc(9))
button_0=Button(root,text="0",padx=40,pady=20,bg='yellow',fg='blue',command=lambda:bc(0))
button_p=Button(root,text="+",padx=40,pady=20,bg='yellow',fg='blue',command=ba)
button_s=Button(root,text="-",padx=40,pady=20,bg='yellow',fg='blue',command=mi)
button_m=Button(root,text="x",padx=40,pady=20,bg='yellow',fg='blue',command=mu)
button_d=Button(root,text="/",padx=40,pady=20,bg='yellow',fg='blue',command=di)
button_po=Button(root,text=".",padx=40,pady=20,bg='yellow',fg='blue',command=po)
buttonc=Button(root,text="C",padx=40,pady=20,bg='yellow',fg='blue',command=clear)
buttone=Button(root,text="=",padx=40,pady=20,bg='yellow',fg='blue',command=eq)
button_sin=Button(root,text="Sin",padx=35,pady=20,bg='yellow',fg='blue',command=si)
button_cos=Button(root,text="Cos",padx=33,pady=20,bg='yellow',fg='blue',command=cos)
button_tan=Button(root,text="Tan",padx=34,pady=20,bg='yellow',fg='blue',command=tan)
button_1.place(x=400,y=400)
button_2.place(x=500,y=400)
button_3.place(x=600,y=400)
button_4.place(x=400,y=330)
button_5.place(x=500,y=330)
button_6.place(x=600,y=330)
button_7.place(x=400,y=260)
button_8.place(x=500,y=260)
button_9.place(x=600,y=260)
button_0.place(x=500,y=470)
button_p.place(x=700,y=470)
button_s.place(x=700,y=400)
button_m.place(x=700,y=330)
button_d.place(x=700,y=260)
button_po.place(x=600,y=470)
buttonc.place(x=700,y=190)
buttone.place(x=400,y=470)
button_sin.place(x=400,y=190)
button_cos.place(x=500,y=190)
button_tan.place(x=600,y=190)
mainloop()