from tkinter import *
import rotatescreen

root = Tk()
root.geometry("500x500")
root.resizable(False, False)
root.config(bg="#333")
root.title("Screen Rotation")

def rotate(enter):
    screen = rotatescreen.get_primary_display()

    if enter == 'up':
        screen.set_landscape()

    elif enter == 'down':
        screen.set_landscape_flipped()

    elif enter == 'left':
        screen.set_portrait()

    elif enter == 'right':
        screen.set_portrait_flipped()

Button(root, text="Up", width=15, height=2, command=lambda:rotate('up'), cursor='hand2').place(x=190, y=50)

Button(root, text="Down", width=15, height=2, command=lambda:rotate('down'), cursor='hand2').place(x=190, y=360)

Button(root, text="Right", width=15, height=2, command=lambda:rotate('right'), cursor='hand2').place(x=360, y=200)

Button(root, text="Left", width=15, height=2, command=lambda:rotate('left'), cursor='hand2').place(x=20, y=200)

root.mainloop()