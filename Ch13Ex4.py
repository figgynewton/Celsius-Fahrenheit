Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from tkinter.messagebox import showinfo
>>> win = Tk()
>>> win.title("Temperature Converter")
''
>>> def c_to_f():
	value = int(entry.get())
	answer = (value * 9/5) + 32
	showinfo("Answer",f"{value} C = {answer} F")

	
>>> def f_to_c():
	value = int(entry.get())
	answer = (value - 32) * 5/9
	showinfo("Answer",f"{value} F = {answer} C")

	
>>> label = Label(win,text="Enter Temperature Here :",font=('arial',12))
>>> label.grid(row=0,column=0)
>>> entry = Entry(win,font=('arial',14))
>>> entry.grid(row=1,column=0)
>>> button1 = Button(win,text="Celsius to Fahrenheit",font=('arial',12),command=c_to_f)
>>> button1.grid(row=3,column=0)
>>> button2 = Button(win,text="Fahrenheit to Celsius",font=('arial',12),command=f_to_c)
>>> button2.grid(row=4,column=0)
>>> win.mainloop()
