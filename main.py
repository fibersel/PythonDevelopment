from tkinter import *
import time

SHUTDOWN_CTR = 5

k = 0



def button_clicker():
	global k
	if SHUTDOWN_CTR <= k:
		exit(13)
	k += 1
	button['text'] = 'clickme, TIME:' + time.strftime('%H:%M:%S')
	print('кек')


root = Tk()
label = Label(text='kekovich')
label.pack(side=TOP)
button1 = Button(root, bg='red', text='clickme, TIME:' + time.strftime('%H:%M:%S'), command=button_clicker)
button1.pack(side=LEFT)
buttom2 = Button(root, bg='blue', text='clickme_2', command=lambda: print('have a nice day!'))
buttom2.pack(side=LEFT)
button3 = Button(root, bg='green', text='clickme_3', command=lambda: print('yet another command'))
button3.pack(side=LEFT)
root.mainloop()

