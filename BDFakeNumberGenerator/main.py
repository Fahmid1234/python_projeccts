from tkinter import *
import random

root = Tk()
root.title("Fake Number Generator (BD)")
root.geometry("700x400")
root.resizable(False, False)
root.config(background="lightgreen")

def generator():

    operator_code = random.choice(['017', '018', '019', '015', '016'])


    num = ''.join(random.choices('0123456789', k=8))

    phone_number = f'+88{operator_code}{num}'
    number.config(text=phone_number)

heading = Label(root, text="Fake Number Generator", bg="lightgreen", font=("Trebuchet MS", 30, "bold"), fg="#364971")
heading.pack(pady=(50, 0))


button = Button(root, text="Generate", font="arial 20 bold", bg="lightblue", fg="lightyellow", command=generator)
button.place(x=280, y=150)
cs = Label(root, text="The number is:", font="poppins 20", bg="lightgreen", fg="#364971")
cs.place(x=100, y=250)

number = Label(root, font=("poppins", 20), bg="lightgreen", fg="#364971")
number.place(x=350, y=250)
root.mainloop()