from tkinter import *
window = Tk()
window.title("Button Action")
window.geometry('300x300')
lbl = Label(window, text="")
lbl.pack()
def clicked():
    lbl.configure(text="Button is clicked !!")
btn = Button(window, text="Click here", command=clicked)
btn.pack()
window.mainloop()