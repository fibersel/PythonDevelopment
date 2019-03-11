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
label.grid()
button = Button(root, bg='red', text='clickme, TIME:' + time.strftime('%H:%M:%S'), command=button_clicker)
button.grid()

root.mainloop()

