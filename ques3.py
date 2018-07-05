from tkinter import *

root = Tk()
root.title('First App')
root.configure(background = 'blue')
frame = Frame(root, bg = 'skyblue')
frame.grid(row = 1, column = 1)

user = Label(frame, text = 'User Name')
user.grid(row = 1, column = 0, sticky = E)
def clicked() :
    user.configure(text = 'Changed')

submit = Button(frame, text = 'Change', bg = 'yellow',\
                 activebackground = 'red', \
                 activeforeground = 'white', command = clicked)
exit = Button(frame, text = 'Log Out', \
               command = root.destroy)

submit.grid(row = 2, column = 0, sticky = W)
exit.grid(row = 2, column = 1, sticky = E)

root.mainloop()
