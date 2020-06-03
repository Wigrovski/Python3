from tkinter import *

root = Tk()
root.title('Calculator')

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def add_button(number):
    #e.delete(0, END)
    e.insert(END, number)


def cl_screen():
    e.delete(0, END)

def add_butt():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def equal_button():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))

def add_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def add_multi():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def add_div():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)



#Define buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: add_button(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: add_button(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: add_button(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: add_button(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: add_button(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: add_button(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: add_button(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: add_button(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: add_button(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: add_button(0))
button_add = Button(root, text="+", padx=40, pady=20, command=add_butt)
button_equal = Button(root, text="=", padx=100, pady=20, command=equal_button)
button_clear = Button(root, text="Clear", padx=87, pady=20, command=cl_screen)

button_sub = Button(root, text="-", padx=40, pady=20, command=add_sub)
button_multi = Button(root, text="*", padx=40, pady=20, command=add_multi)
button_div = Button(root, text="/", padx=40, pady=20, command=add_div)


#Buttons on screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2 , column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

button_sub.grid(row=6, column=0)
button_multi.grid(row=6, column=1)
button_div.grid(row=6, column=2)

root.mainloop()