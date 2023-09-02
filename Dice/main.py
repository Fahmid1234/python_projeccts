# print("\u25CF \u2500 \u2510 \u250C \u2502 \u2514 \u2518")
import random
from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.geometry('300x200')
root.title("Dice A roll")
ran = random.randint(1, 6)
# dict = { 1:('''┌─────────┐
# │         │
# │    ●    │
# │         │
# └─────────┘'''),
#          2:('''┌─────────┐
# │       ● │
# │         │
# │ ●       │
# └─────────┘'''),
#          3:('''┌─────────┐
# │       ● │
# │    ●    │
# │ ●       │
# └─────────┘'''),
#          4:('''┌─────────┐
# │ ●     ● │
# │         │
# │ ●     ● │
# └─────────┘'''),
#          5:('''┌─────────┐
# │ ●     ● │
# │    ●    │
# │ ●     ● │
# └─────────┘'''),
#          6:('''┌─────────┐
# │ ●     ● │
# │ ●     ● │
# │ ●     ● │
# └─────────┘''')
#          }
def roll():
    dict1 = { 1: '1.png',
         2:'2.png',
         3:'3.png',
         4:'4.png',
         5:'5.png',
         6:'6.png'
        }
    ran = random.randint(1, 6)
    image = Image.open(dict1[ran])
    tk_image = ImageTk.PhotoImage(image)
    
    label.config(image=tk_image)
    label.image=tk_image


label = Label(root)
label.pack(expand=True)
button = Button(root, text="Roll Dice", command=roll, cursor='hand2')
button.pack(expand=True)
root.mainloop()




# root = Tk()
# root.title("Image Viewer")
#
# # Replace 'your_image.png' with the path to your image file
# image = Image.open('1.png')
# tk_image = ImageTk.PhotoImage(image)
#
# label = Label(root, image=tk_image)
# label.pack()
#
# root.mainloop()
