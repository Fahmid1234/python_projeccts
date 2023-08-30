import smtplib
import random
from tkinter import *

otp = random.randint(00000, 99999)
server =smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('mdfahmidbinmostafa@gmail.com', 'glffppadhqigbvei')


root = Tk()
root.title("Spell Checker")
# root.geometry("700x400")
root.state('zoomed')
root.resizable(False, False)
root.config(background="#dae6f6")

def is_valid_email(email_name):
    
    def is_valid_user_name(n):
        if len(n)>0:
            for i in n:
                if i.isalnum() or i =="." or i =="_" or i =="-":
                    pass
                else:
                    return False
            else:
                return True
        else:
            return False

    def is_valid_domain_name(n):
        if len(n)>0 and n.count(".")>0 and ".." not in n and n[0] != '.':
            for i in n:
                if i.isalnum() or i =="." or i =="-":
                    pass
                else:
                    return False
            else:
                return True
        else:
            return False



    if email_name[0].isalnum() and email_name[-1].isalpha() and email_name.count("@") == 1:

        user_name, domain_name = email_name.split("@")

        if is_valid_domain_name(domain_name) and is_valid_user_name(user_name):
            return True

        else:
            return False
    else:
        return False


def check_email():
    global server
    email = enter_text.get()
    if is_valid_email(email):
        server.sendmail('mdfahmidbinmostafa@gmail.com', email, str(otp))
        text.pack(pady=(10, 0))
        otp_entry.pack(pady=10)
        button1.pack(pady=10)

def correct():
    if(str(otp) == otp_entry.get()):
            email_validation.config(text='Valid email')
    else:
        email_validation.config(text='Invalid email')


heading = Label(root, text="Email Validation", bg="#dae6f6", font=("Trebuchet MS", 30, "bold"), fg="#364971")
heading.pack(pady=(50, 0))

enter_text = Entry(root, justify='center', width=30, font=("poppins", 25), bg="white")
enter_text.pack(pady=10)
enter_text.focus()



button = Button(root, text="Send Code", font="arial 20 bold", fg="white", bg="red", cursor='hand2', command=check_email)
button.pack()


text = Label(root, text="An OTP has been send to your email. Please check your email and write here.", bg="#dae6f6", font=("Trebuchet MS", 30, "bold"), fg="#364971")

otp_entry = Entry(root, justify='center', width=10, font=("poppins", 25), bg="white")

button1 = Button(root, text="Check", font="arial 20 bold", fg="white", bg="red", cursor='hand2', command=correct)


email_validation = Label(root, font=("poppins", 25), bg="#dae6f6", fg="#364971")
email_validation.place(x=670, y=450)
root.mainloop()

