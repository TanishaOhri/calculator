from tkinter import *
root= Tk()

#calculator
root.title("Calculator")
# to show input of numbers
ent=Entry(root,width=60)
ent.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

# def all functions of clicking no, add, sub, multiply, divide, clear, result and equal 
def add():
    first_num=ent.get() 
    global f_num
    f_num=int(first_num)
    ent.delete(0,END)
    global calc
    calc=1
    
def sub():
    first_num=ent.get() 
    global f_num
    f_num=int(first_num)
    ent.delete(0,END)
    global calc
    calc=2

def div():
    first_num=ent.get() 
    global f_num
    f_num=int(first_num)
    ent.delete(0,END)
    global calc
    calc=3

def mul():
    first_num=ent.get() 
    global f_num
    f_num=int(first_num)
    ent.delete(0,END)
    global calc
    calc=4

def result():
    second_num=ent.get()
    ent.delete(0,END)
    s_num=int(second_num)
    if(calc==1):
        ent.insert(0,f_num+s_num)
    elif(calc==2):
        ent.insert(0,f_num-s_num)
    elif(calc==3):
        ent.insert(0,f_num/s_num)
    elif(calc==4):
        ent.insert(0,f_num*s_num)

def clear():
    ent.delete(0,END)
def button_click(number):
    # ent.delete(0,END)
    current=ent.get()
    ent.delete(0,END)
    ent.insert(0,str(current) + str(number))

#showing all the buttons
but1=Button(root,text="1",width=10,padx=40,pady=20,command=lambda: button_click(1))
but1.grid(row=3,column=2)
but2=Button(root,text="2",width=10,padx=40,pady=20,command=lambda: button_click(2))
but2.grid(row=3,column=1)
but3=Button(root,text="3",width=10,padx=40,pady=20,command=lambda: button_click(3))
but3.grid(row=3,column=0)
but4=Button(root,text="4",width=10,padx=40,pady=20,command=lambda: button_click(4))
but4.grid(row=2,column=0)
but5=Button(root,text="5",width=10,padx=40,pady=20,command=lambda: button_click(5))
but5.grid(row=2,column=1)
but6=Button(root,text="6",width=10,padx=40,pady=20,command=lambda: button_click(6))
but6.grid(row=2,column=2)
but7=Button(root,text="7",width=10,padx=40,pady=20,command=lambda: button_click(7))
but7.grid(row=1,column=0)
but8=Button(root,text="8",width=10,padx=40,pady=20,command=lambda: button_click(8))
but8.grid(row=1,column=1,)
but9=Button(root,text="9",width=10,padx=40,pady=20,command=lambda: button_click(9))
but9.grid(row=1,column=2)
but0=Button(root,text="0",width=10,padx=40,pady=20,command=lambda: button_click(0))
but0.grid(row=4,column=0,)
but_clear=Button(root,text="Clear",command=clear,width=32,padx=40,pady=20)
but_clear.grid(row=4,column=1,columnspan=2)
but_sub=Button(root,text="-",command=sub,width=10,padx=40,pady=20)
but_sub.grid(row=5,column=2)
but_equal=Button(root,text="=",command=result,width=32,padx=40,pady=20)
but_equal.grid(row=6,column=0,columnspan=2)
but_add=Button(root,text="+",command=add,width=10,padx=40,pady=20)
but_add.grid(row=5,column=1)
but_div=Button(root,text="/",command=div,width=10,padx=40,pady=20)
but_div.grid(row=5,column=0)
but_mul=Button(root,text="*",command=mul,width=10,padx=40,pady=20)
but_mul.grid(row=6,column=2)

root.mainloop()
