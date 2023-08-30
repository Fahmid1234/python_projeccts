from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic-Tac-Toe Game")
root.resizable(False, False)
count = 0
clicked = True

def disable():
    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)
    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)
    btn6.config(state=DISABLED)
    btn7.config(state=DISABLED)
    btn8.config(state=DISABLED)
    btn9.config(state=DISABLED)
def win_check():
    global win
    win = False
    if btn1['text'] == 'X' and btn2['text'] == 'X' and btn3['text'] == 'X':
        win = True
        messagebox.showinfo('Tic-Tac-Toe', "Congratulation! X Won the game")
        disable()
    elif btn1['text'] == 'X' and btn4['text'] == 'X' and btn7['text'] == 'X':
        win = True
        messagebox.showinfo('Tic-Tac-Toe', "Congratulation! X Won the game")
        disable()
    elif btn4['text'] == 'X' and btn5['text'] == 'X' and btn6['text'] == 'X':
        win = True
        messagebox.showinfo('Tic-Tac-Toe', "Congratulation! X Won the game")
        disable()
    elif btn1['text'] == 'X' and btn5['text'] == 'X' and btn9['text'] == 'X':
        win = True
        messagebox.showinfo('Tic-Tac-Toe', "Congratulation! X Won the game")
        disable()
    elif btn2['text'] == 'X' and btn5['text'] == 'X' and btn8['text'] == 'X':
        win = True
        messagebox.showinfo('Tic-Tac-Toe', "Congratulation! X Won the game")
        disable()
    elif btn3['text'] == 'X' and btn6['text'] == 'X' and btn9['text'] == 'X':
        win = True
        messagebox.showinfo('Tic-Tac-Toe', "Congratulation! X Won the game")
        disable()
    elif btn7['text'] == 'X' and btn8['text'] == 'X' and btn9['text'] == 'X':
        win = True
        messagebox.showinfo('Tic-Tac-Toe', "Congratulation! X Won the game")
        disable()
    elif btn3['text'] == 'X' and btn5['text'] == 'X' and btn7['text'] == 'X':
        win = True
        messagebox.showinfo('Tic-Tac-Toe', "Congratulation! X Won the game")
        disable()
    elif btn1['text'] == 'O' and btn2['text'] == 'O' and btn3['text'] == 'O':
        win = True
        messagebox.showinfo('Tic-Tac-Toe', "Congratulation! O Won the game")
        disable()
    elif btn4['text'] == 'O' and btn5['text'] == 'O' and btn6['text'] == 'O':
        win = True
        messagebox.showinfo('Tic-Tac-Toe', "Congratulation! O Won the game")
        disable()
    elif btn1['text'] == 'O' and btn4['text'] == 'O' and btn7['text'] == 'O':
        win = True
        messagebox.showinfo('Tic-Tac-Toe', "Congratulation! O Won the game")
        disable()
    elif btn1['text'] == 'O' and btn5['text'] == 'O' and btn9['text'] == 'O':
        win = True
        messagebox.showinfo('Tic-Tac-Toe', "Congratulation! O Won the game")
        disable()
    elif btn2['text'] == 'O' and btn5['text'] == 'O' and btn8['text'] == 'O':
        win = True
        messagebox.showinfo('Tic-Tac-Toe', "Congratulation! O Won the game")
        disable()
    elif btn3['text'] == 'O' and btn6['text'] == 'O' and btn9['text'] == 'O':
        win = True
        messagebox.showinfo('Tic-Tac-Toe', "O Won the game")
        disable()
    elif btn7['text'] == 'O' and btn8['text'] == 'O' and btn9['text'] == 'O':
        win = True
        messagebox.showinfo('Tic-Tac-Toe', "Congratulation! O Won the game")
        disable()
    elif btn3['text'] == 'O' and btn5['text'] == 'O' and btn7['text'] == 'O':
        win = True
        messagebox.showinfo('Tic-Tac-Toe', "Congratulation! O Won the game")
        disable()

def click(b):
    global count, clicked

    if b['text'] == '' and clicked == True:
        b['text'] = 'X'
        count += 1
        clicked = False
        win_check()
    elif b['text'] == '' and clicked == False:
        b['text'] = 'O'
        count += 1
        clicked = True
        win_check()
    else:
        messagebox.showerror("Tic-Tac-Toe", "Wrong clicked!")

def reset():
    global btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, clicked, count
    btn1 = Button(root, text='', width=15, height=6, bg='skyblue', command=lambda: click(btn1))
    btn1.grid(column=0, row=0)

    btn2 = Button(root, text='', width=15, height=6, bg='skyblue', command=lambda: click(btn2))
    btn2.grid(column=0, row=1)

    btn3 = Button(root, text='', width=15, height=6, bg='skyblue', command=lambda: click(btn3))
    btn3.grid(column=0, row=2)

    btn4 = Button(root, text='', width=15, height=6, bg='skyblue', command=lambda: click(btn4))
    btn4.grid(column=1, row=0)

    btn5 = Button(root, text='', width=15, height=6, bg='skyblue', command=lambda: click(btn5))
    btn5.grid(column=1, row=1)

    btn6 = Button(root, text='', width=15, height=6, bg='skyblue', command=lambda: click(btn6))
    btn6.grid(column=1, row=2)

    btn7 = Button(root, text='', width=15, height=6, bg='skyblue', command=lambda: click(btn7))
    btn7.grid(column=2, row=0)

    btn8 = Button(root, text='', width=15, height=6, bg='skyblue', command=lambda: click(btn8))
    btn8.grid(column=2, row=1)

    btn9 = Button(root, text='', width=15, height=6, bg='skyblue', command=lambda: click(btn9))
    btn9.grid(column=2, row=2)
btn = Button(root, text="Reset game", command=reset, width=10, height=3,bg='#333', fg='#eeeeee')
btn.grid(column=1, row=4)
reset()
root.mainloop()