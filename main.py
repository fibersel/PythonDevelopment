from tkinter import *

def button_clicker():
	print('кек')


root = Tk()

button1 = Button(root, bg='red', text='clickme', command=button_clicker)
button1.pack()

root.mainloop()

