import pyttsx3
import ttkbootstrap as tb
from tkinter import *
from datetime import datetime
import datetime

root = tb.Window(themename='superhero')
root.title("Text to Speech")
root.geometry("1000x800")
engine = pyttsx3.init()
engine.getProperty("rate")
engine.setProperty("rate", 120)
def say():
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[0].id)
    text = Text_Box.get('1.0', END)
    engine.say(text)

    engine.runAndWait()
def says():
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[1].id)

    text = Text_Box.get('1.0', END)
    engine.say(text)

    engine.runAndWait()

Text_Box = tb.Text(root, font=("Helvetica", 12))
Text_Box.pack(pady=20)

Speak_Button = tb.Button(root, text="Male Listen", cursor='hand2', bootstyle='success outline', command=say)
Speak_Button.place(x=53, y=600)

Speak_Button1 = tb.Button(root, text="Female Listen", cursor='hand2', bootstyle='success outline', command=says)
Speak_Button1.place(x=832, y=600)
# pyttsx3.speak("Hello guys, welcome to this project. You will know how to make a exe file in pytho with the help of tkinter")
root.mainloop()

