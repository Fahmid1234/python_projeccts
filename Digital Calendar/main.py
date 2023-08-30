from tkinter import *
from tkcalendar import *

root = Tk()
root.title("Calendar")
root.geometry("250x180")
root.resizable(False, False)
mycal = Calendar(root, setmode='day', date_pattern='d/m/yy')
mycal.pack()

root.mainloop()