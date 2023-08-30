from tkinter import *
import ttkbootstrap as tb
from tkinter import messagebox

root = tb.Window(themename="superhero")
root.geometry("1000x500")


root.resizable(False, False)

frame_width = 300
frame_height = 370

style = tb.Style()
style.configure("TButton", font=("Arial", 14, "bold"))

tb.Label(root, text="Bill Management System", font=('calibri', 33), width=300).pack(padx=150)

f = tb.Frame(root, height=frame_height, width=frame_width, relief=RAISED, bootstyle="light")  # Adjusted width to 320
f.place(x=5, y=118)

menu = tb.Label(f, text="Menu", font=("Gabriola", 40, 'bold'), bootstyle="warning", background="#ABB6C2")
menu.place(x=80, y=-15)

item1 = tb.Label(f, text="Pasta----------80 TK/Plate", font=("Lucida Calligraphy", 12, 'bold'), background="#ABB6C2")
item1.place(x=10, y=80)

item2 = tb.Label(f, text="Burger------150 TK/Piece", font=("Lucida Calligraphy", 12, 'bold'), background="#ABB6C2")
item2.place(x=10, y=110)

item3 = tb.Label(f, text="Cake----------120 TK/Piece", font=("Lucida Calligraphy", 12, 'bold'), background="#ABB6C2")
item3.place(x=10, y=140)

item4 = tb.Label(f, text="Tea-------------60 TK/Cup", font=("Lucida Calligraphy", 12, 'bold'), background="#ABB6C2")
item4.place(x=10, y=170)

item5 = tb.Label(f, text="Coffee--------120 TK/Cup", font=("Lucida Calligraphy", 12, 'bold'), background="#ABB6C2")
item5.place(x=10, y=200)

item6 = tb.Label(f, text="Drinks--------50 TK/Glass", font=("Lucida Calligraphy", 12, 'bold'), background="#ABB6C2")
item6.place(x=10, y=230)

item7 = tb.Label(f, text="Custard-----150 TK/Bowl", font=("Lucida Calligraphy", 12, 'bold'), background="#ABB6C2")
item7.place(x=10, y=260)

f1 = Frame(root, relief=RAISED, width=frame_width, height=frame_height, background="skyblue")
f1.place(x=330, y=118)

pasta = StringVar()
burger = StringVar()
tea = StringVar()
coffee = StringVar()
cake = StringVar()
drinks = StringVar()
custard = StringVar()
disc = StringVar()
total_bill = StringVar()

def reset():
    entry_pasta.delete(0, END)
    entry_burger.delete(0, END)
    entry_cake.delete(0, END)
    entry_tea.delete(0, END)
    entry_coffee.delete(0, END)
    entry_drinks.delete(0, END)
    entry_custard.delete(0, END)
    entry_disc.delete(0, END)

def total():
    try:a1=int(pasta.get())
    except:a1=0

    try:a2=int(burger.get())
    except:a2=0

    try:a3=int(cake.get())
    except:a3=0

    try:a4=int(tea.get())
    except:a4=0

    try:a5=int(coffee.get())
    except:a5=0

    try:a6=int(drinks.get())
    except:a6=0

    try:a7=int(custard.get())
    except:a7=0

    try:a8=int(disc.get())
    except:a8=0

    c1 = 80 * a1
    c2 = 150 * a2
    c3 = 120 * a3
    c4 = 60 * a4
    c5 = 120 * a5
    c6 = 50 * a6
    c7 = 150 * a7
    c8 = 1 * a8
    total = (c1 + c2 + c3 + c4 + c5 + c6 + c7)-((c8/100)*(c1 + c2 + c3 + c4 + c5 + c6 + c7))
    print(c8, total)
    str_bill = str('%.2f' %total), "TK"

    total_entry = tb.Entry(f2, textvariable=total_bill, state='readonly', width=16, font=("aria", 15, "bold"), justify='center', bootstyle="primary")
    total_entry.place(x=30, y=150)

    messagebox.showinfo("Bill", str_bill)
    total_bill.set(str_bill)

lbl_pasta = tb.Label(f1, text="Pasta", font=("aria", 14, "bold"), width=10, background="#4E5D6C")
lbl_pasta.grid(row=1, column=0)

entry_pasta = tb.Entry(f1, font=("aria", 14, "bold"), width=8, bootstyle="warning")
entry_pasta.grid(row=1, column=1)

lbl_burger = tb.Label(f1, text="Burger", font=("aria", 14, "bold"), width=10, background="#4E5D6C")
lbl_burger.grid(row=2, column=0)

entry_burger = tb.Entry(f1, font=("aria", 14, "bold"), width=8, textvariable=burger, bootstyle="warning")
entry_burger.grid(row=2, column=1)

lbl_cake = tb.Label(f1, text="Cake", font=("aria", 14, "bold"), width=10, background="#4E5D6C")
lbl_cake.grid(row=3, column=0)

entry_cake = tb.Entry(f1, font=("aria", 14, "bold"), width=8, textvariable=cake, bootstyle="warning")
entry_cake.grid(row=3, column=1)

lbl_tea = tb.Label(f1, text="Tea", font=("aria", 14, "bold"), width=10, background="#4E5D6C")
lbl_tea.grid(row=4, column=0)

entry_tea = tb.Entry(f1, font=("aria", 14, "bold"), width=8, textvariable=tea, bootstyle="warning")
entry_tea.grid(row=4, column=1)

lbl_coffee = tb.Label(f1, text="Coffee", font=("aria", 14, "bold"), width=10, background="#4E5D6C")
lbl_coffee.grid(row=5, column=0)

entry_coffee = tb.Entry(f1, font=("aria", 14, "bold"), width=8, textvariable=coffee, bootstyle="warning")
entry_coffee.grid(row=5, column=1)

lbl_drinks = tb.Label(f1, text="Drinks", font=("aria", 14, "bold"), width=10, background="#4E5D6C")
lbl_drinks.grid(row=6, column=0)

entry_drinks = tb.Entry(f1, font=("aria", 14, "bold"), width=8, textvariable=drinks, bootstyle="warning")
entry_drinks.grid(row=6, column=1)

lbl_custard = tb.Label(f1, text="Custard", font=("aria", 14, "bold"), width=10, background="#4E5D6C")
lbl_custard.grid(row=7, column=0)

entry_custard = tb.Entry(f1, font=("aria", 14, "bold"), width=8, textvariable=custard, bootstyle="warning")
entry_custard.grid(row=7, column=1)

lbl_disc = tb.Label(f1, text="Discount(%)", font=("aria", 14, "bold"), width=11, background="#4E5D6C")
lbl_disc.grid(row=8, column=0)

entry_disc = tb.Entry(f1, font=("aria", 14, "bold"), width=8, textvariable=disc, bootstyle="warning")
entry_disc.grid(row=8, column=1)

btn1 = tb.Button(f1, text="Reset", width=8, bootstyle="info", command=reset)
btn1.grid(row=9, column=0)

btn2 = tb.Button(f1, text="Total", width=8, bootstyle="success", command=total)
btn2.grid(row=9, column=1)

f2 = tb.Frame(root, height=frame_height, width=frame_width, bootstyle="dark")
f2.place(x=670, y=118)

tb.Label(f2, text='Bill', font=("Gabriola", 40, 'bold'), background="#20374C").place(x=150, y=60, anchor='center')
tb.Label(f2, text='Total', font=("Gabriola", 20, 'bold'), background="#20374C").place(x=150, y=120, anchor='center')



root.mainloop()