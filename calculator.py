from tkinter import *

def onClick(number):
	global operator
	operator = operator + str(number)
	numbers.set(operator)

def clearInput():
	global operator
	operator = ""
	numbers.set("")

def showResult():
	global operator
	sum = str(eval(operator))
	numbers.set(sum)
	operator = ""


screen = Tk()
screen.title("Basic Calculator")
screen.geometry("365x425+400+200")

operator = ""
numbers = StringVar()

display = Entry(screen, font=("arial", 24, "bold"), textvariable=numbers, insertwidth=4, justify="right").grid(columnspan=4)

button7 = Button(screen, padx=16, pady=16, font=("arial", 24, "bold"), text="7", command=lambda:onClick(7)).grid(row=1, column=0)
button8 = Button(screen, padx=16, pady=16, font=("arial", 24, "bold"), text="8", command=lambda:onClick(8)).grid(row=1, column=1)
button9 = Button(screen, padx=16, pady=16, font=("arial", 24, "bold"), text="9", command=lambda:onClick(9)).grid(row=1, column=2)
dividebtn = Button(screen, padx=16, pady=16, font=("arial", 24, "bold"), text="÷", command=lambda:onClick("/")).grid(row=1, column=3)

button4 = Button(screen, padx=16, pady=16, font=("arial", 24, "bold"), text="4", command=lambda:onClick(4)).grid(row=2, column=0)
button5 = Button(screen, padx=16, pady=16, font=("arial", 24, "bold"), text="5", command=lambda:onClick(5)).grid(row=2, column=1)
button6 = Button(screen, padx=16, pady=16, font=("arial", 24, "bold"), text="6", command=lambda:onClick(6)).grid(row=2, column=2)
mltbtn = Button(screen, padx=16, pady=16, font=("arial", 24, "bold"), text="x", command=lambda:onClick("*")).grid(row=2, column=3)

button1 = Button(screen, padx=16, pady=16, font=("arial", 24, "bold"), text="1", command=lambda:onClick(1)).grid(row=3, column=0)
button2 = Button(screen, padx=16, pady=16, font=("arial", 24, "bold"), text="2", command=lambda:onClick(2)).grid(row=3, column=1)
button3 = Button(screen, padx=16, pady=16, font=("arial", 24, "bold"), text="3", command=lambda:onClick(3)).grid(row=3, column=2)
subbtn = Button(screen, padx=16, pady=16, font=("arial", 24, "bold"), text="_", command=lambda:onClick("-")).grid(row=3, column=3)

clrbtn = Button(screen, padx=16, pady=16, font=("arial", 24, "bold"), text="C", command=lambda:clearInput()).grid(row=4, column=0)
button0 = Button(screen, padx=16, pady=16, font=("arial", 24, "bold"), text="0", command=lambda:onClick(0)).grid(row=4, column=1)
eqbtn = Button(screen, padx=16, pady=16, font=("arial", 24, "bold"), text="=", command=lambda:showResult()).grid(row=4, column=2)
addbtn = Button(screen, padx=16, pady=16, font=("arial", 24, "bold"), text="+", command=lambda:onClick("+")).grid(row=4, column=3)





screen.mainloop()
