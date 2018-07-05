from tkinter import *

root = Tk()
hwL = Label(root, text='Hello World!!')
hwL.pack()
exit = Button(root, text='exit', width=25, \
               command=root.destroy)
exit.pack()
root.mainloop()