from tkinter import *

root = Tk()
result = 0
equation = "" #storing the inputs of the user in a string
root.title("Yokio Calculator")
root.geometry('480x310')
root.resizable(False,False) #prevents the user from resizing the size of the program box
input =Entry(root, width=35,borderwidth=10, font=('arial',10))
root.configure(bg='#1C1C1C')
input.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def btn_click(value):
    global equation
    equation += str(value) #concatenating the value of each input
    input.delete(0,END) #deleting the current input on screen
    input.insert(0,equation)  #displaying the string 'equation' on screen

def clear():
    input.delete(0,END)
    global equation
    equation = ""

def equals():
    global equation
    global result
    if equation != '':
        try:
            result = eval(equation)
            input.delete(0,END)
            input.insert(0,result)
            equation = input.get()
        except: #handling situations where user inputs a mathematical error
            input.insert(0,'Error')
            equation=''
            result = 0
    
def answer():
    global result
    input.delete(0,END)
    input.insert(0,result)

def remove_last():
    global equation
    current = input.get()
    current = current.replace(current[-1],'')
    equation = current
    input.delete(0,END)
    input.insert(0,current)


btn_1 = Button(root,text='1', padx=40, pady=20, command=lambda: btn_click(1), bg='#1C1C1C' ,fg='white')
btn_2 = Button(root,text='2', padx=40, pady=20, command=lambda: btn_click(2), bg='#1C1C1C' ,fg='white')
btn_3 = Button(root,text='3', padx=40, pady=20, command=lambda: btn_click(3), bg='#1C1C1C' ,fg='white')
btn_4 = Button(root,text='4', padx=40, pady=20, command=lambda: btn_click(4), bg='#1C1C1C' ,fg='white')
btn_5 = Button(root,text='5', padx=40, pady=20, command=lambda: btn_click(5), bg='#1C1C1C' ,fg='white')
btn_6 = Button(root,text='6', padx=40, pady=20, command=lambda: btn_click(6), bg='#1C1C1C' ,fg='white')
btn_7 = Button(root,text='7', padx=40, pady=20, command=lambda: btn_click(7), bg='#1C1C1C' ,fg='white')
btn_8 = Button(root,text='8', padx=40, pady=20, command=lambda: btn_click(8), bg='#1C1C1C' ,fg='white')
btn_9 = Button(root,text='9', padx=40, pady=20, command=lambda: btn_click(9), bg='#1C1C1C' ,fg='white')
btn_0 = Button(root,text='0', padx=40, pady=20, command=lambda: btn_click(0), bg='#1C1C1C' ,fg='white')

decimal_btn = Button(root,text='.', padx=40, pady=20, command=lambda: btn_click('.'), bg='#505050', fg='white')
del_btn = Button(root,text='C', padx=40, pady=20, command=lambda: remove_last(), bg='#505050', fg='white')
ans_btn = Button(root,text='Ans', padx=33, pady=20, command=lambda: answer(), bg='#505050', fg='white')
clear_btn = Button(root,text='AC', padx=33, pady=20, command=lambda: clear(), bg='#505050', fg='white')
add_btn = Button(root,text='+',padx=40,pady=20,command=lambda: btn_click('+'), bg='#505050', fg='white')
multiply_btn = Button(root,text='x',padx=40,pady=20,command=lambda: btn_click('*'), bg='#505050', fg='white')
divide_btn = Button(root,text='÷',padx=40,pady=20,command=lambda: btn_click('/'), bg='#505050', fg='white')
subtract_btn = Button(root,text='-',padx=40,pady=20,command=lambda: btn_click('-'), bg='#505050', fg='white')
equal_btn = Button(root,text='=',padx=90,pady=20,command=lambda: equals(), bg='#Ffa500')

#positioning the buttons
multiply_btn.grid(row=3,column=3)
add_btn.grid(row=2,column=3)
del_btn.grid(row=1,column=3)
decimal_btn.grid(row=4,column=1)
ans_btn.grid(row=4,column=2,)
clear_btn.grid(row=1,column=4,)
divide_btn.grid(row=3,column=4)
subtract_btn.grid(row=2,column=4)
equal_btn.grid(row=4,column=3,columnspan=2)

btn_1.grid(row=3,column=0)
btn_2.grid(row=3,column=1)
btn_3.grid(row=3,column=2)

btn_4.grid(row=2,column=0)
btn_5.grid(row=2,column=1)
btn_6.grid(row=2,column=2)

btn_7.grid(row=1,column=0)
btn_8.grid(row=1,column=1)
btn_9.grid(row=1,column=2)
btn_0.grid(row=4,column=0)

root.mainloop()