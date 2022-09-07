from tkinter import *
import tkinter.font as tkFont
import tkinter.messagebox as msgbox
import random

def randMove(t):
    x = random.randint(50,150)
    y = random.randint(50,100)
    no.place(x=x, y=y)
    
def yeFunc():
    ye.destroy()
    no.destroy()

    label.config(text = "i knew it :)))")

    win.protocol("WM_DELETE_WINDOW", lambda:win.destroy())
def noFunc():
    no.config(state=DISABLED)
    randMove(1)

def close():
    msgbox.showwarning(title="hehe", message="nope :)")

win=Tk()
win.geometry("300x150")
win.resizable(width=False, height=False)

label = Label(win, text="Ar u gay?", font=('Times', 35))
label.pack()

ye = Button(win, text="yes", font=('Times', 15), command=yeFunc)
ye.pack()
ye.place(x=70,y=70)

no = Button(win, text="no", font=('Times', 15), command=noFunc)
no.bind('<Enter>', randMove)
no.pack()
no.place(x=170,y=70)

win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()