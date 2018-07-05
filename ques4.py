from tkinter import *

def show_entry_fields():
   print("text is %s" % (en.get()))

root = Tk()
Label(root, text="Write Something:").grid(row=0)

en = Entry(root)
en.grid(row=0, column=1)

Button(root, text='exit', command=root.quit).grid(row=3, column=0, sticky=W,)
Button(root, text='print', command=show_entry_fields).grid(row=3, column=1, sticky=E, )

mainloop( )