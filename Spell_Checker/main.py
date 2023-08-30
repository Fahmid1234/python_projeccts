from tkinter import *
from spellchecker import SpellChecker

root = Tk()
root.title("Spell Checker")
# root.geometry("700x400")
root.state('zoomed')
root.resizable(False, False)
root.config(background="#dae6f6")

spell_word = SpellChecker()
def check_spell():
    word = enter_text.get()
    right = spell_word.correction(word)
    same_word = spell_word.candidates(word)
    cs = Label(root, text="Correct text is:", font="poppins 20", bg="#dae6f6", fg="#364971")
    cs.place(x=550, y=250)
    spell.config(text=right)
    same_word.remove(right)
    similar_words_str = ", ".join(same_word)
    if similar_words_str == '':
        simillar_word.config(text="Simillar Word:    "+'No simillar word found')

    else:
        simillar_word.config(text="Simillar Word:    "+similar_words_str)

heading = Label(root, text="Spell Checker", bg="#dae6f6", font=("Trebuchet MS", 30, "bold"), fg="#364971")
heading.pack(pady=(50, 0))

enter_text = Entry(root, justify='center', width=30, font=("poppins", 25), bg="white")
enter_text.pack(pady=10)
enter_text.focus()

button = Button(root, text="Check", font="arial 20 bold", fg="white", bg="red", command=check_spell)
button.pack()

spell = Label(root, font=("poppins", 20), bg="#dae6f6", fg="#364971")
spell.place(x=750, y=250)

simillar_word = Label(root, font=("poppins", 20), bg="#dae6f6", fg="#364971")
simillar_word.place(x=350, y=300)
root.mainloop()