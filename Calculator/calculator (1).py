from tkinter import *
root=Tk()
root.title("simple calculator")
e=Entry()
e.grid(row=0,column=0,padx=10,pady=10,columnspan=3)
def button_click(number):
  current=e.get()
  e.delete(0,END)
  e.insert(0,str(current)+str(number))
def button_clear():
  e.delete(0,END)
def button_add():
   first_number=e.get()
   global f_num
   global math
   math="add"
   f_num=int(first_number)
   e.delete(0,END)
def button_equal():
   second_number=e.get()
   e.delete(0,END)
   if math=="add":
     e.insert(0,f_num+int(second_number))
   if math=="sub":
     e.insert(0,f_num-int(second_number))
   if math=="mul":
     e.insert(0,f_num*int(second_number))
   if math=="div":
     e.insert(0,f_num//int(second_number))
def button_sub():
   first_number=e.get()
   global f_num
   global math
   math="sub"
   f_num=int(first_number)
   e.delete(0,END)
def button_mul():
   first_number=e.get()
   global f_num
   global math
   math="mul"
   f_num=int(first_number)
   e.delete(0,END)
def button_div():
   first_number=e.get()
   global f_num
   global math
   math="div"
   f_num=int(first_number)
   e.delete(0,END)

button_1=Button(text="1",padx=40,pady=20,command=lambda: button_click(1))
button_2=Button(text="2",padx=40,pady=20,command=lambda: button_click(2))
button_3=Button(text="3",padx=40,pady=20,command=lambda: button_click(3))

button_4=Button(text="4",padx=40,pady=20,command=lambda: button_click(4))
button_5=Button(text="5",padx=40,pady=20,command=lambda: button_click(5))
button_6=Button(text="6",padx=40,pady=20,command=lambda: button_click(6))

button_7=Button(text="7",padx=40,pady=20,command=lambda: button_click(7))
button_8=Button(text="8",padx=40,pady=20,command=lambda: button_click(8))
button_9=Button(text="9",padx=40,pady=20,command=lambda: button_click(9))
button_0=Button(text="0",padx=40,pady=20,command=lambda: button_click(0))
button_add=Button(text="+",padx=39,pady=20,command=button_add)
button_sub=Button(text="-",padx=39,pady=20,command=button_sub)
button_mul=Button(text="*",padx=39,pady=20,command=button_mul)
button_div=Button(text="/",padx=39,pady=20,command=button_div)
button_equal=Button(text="=",padx=90,pady=20,command=button_equal)
button_clear=Button(text="clear",padx=79,pady=20,command=button_clear)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2,columnspan=3)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2,columnspan=3)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2,columnspan=3)
button_0.grid(row=4,column=0)

button_add.grid(row=6,column=0)
button_equal.grid(row=6,column=1,columnspan=2)
button_sub.grid(row=5,column=0)
button_mul.grid(row=5,column=1)
button_div.grid(row=5,column=2,columnspan=3)
button_clear.grid(row=4,column=1,columnspan=2)

root.mainloop()