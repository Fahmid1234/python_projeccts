# import all package necessary packages
import calendar
import os
from datetime import date
import datetime
import operator
import random
import urllib
import cv2
import numpy as np
import psutil
import pyautogui
# import googletrans
from bs4 import BeautifulSoup
import webbrowser
from gtts import gTTS
import pyjokes
import pyttsx3
import pywhatkit
import requests
import speech_recognition as sr
import speedtest
import wikipedia
import googletrans
import wolframalpha as wolframalpha
from playsound import playsound
from pywikihow import search_wikihow
import playsound
import keyboard
# import gtts
from tkinter import *

translator = googletrans.Translator()


# Gui for assistance
class AssistanceMama:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Assistance 2023")
        self.root.wm_state('zoomed')

        # pyttsx3 initial
        listener = sr.Recognizer()
        engine = pyttsx3.init()

        # voice speed setup
        engine.getProperty("rate")
        engine.setProperty("rate", 120)

        def stop_speaking():
            engine.stop()

        # list of songs, greeting and congratulate
        songs = [" "]
        rand = ["Hi", "Hello", "Hey", "Hello, my friend!!!", "Hey guys"]
        cong = ["welcome", "thanks", "thank you", "thank you too", "thank you very much"]

        # find the address of this device
        url = requests.get('http://ipinfo.io/json')
        data = url.json()
        city = data['region']
        country = data['country']

        # find the current day name
        dates = calendar.day_name[date.today().weekday()]

        # function of saying my AI
        def talk(text):
            engine.say(text)
            engine.runAndWait()

        # function of taking command from users
        def take_command():
            try:
                with sr.Microphone() as source:
                    print('Clearing Background Noise...')
                    listener.adjust_for_ambient_noise(source, duration=1)
                    print('listening...')
                    voice = listener.listen(source)
                    command = listener.recognize_google(voice, language='en')
                    BtnShow.config(text='Speak')
                    command = command.lower()
                    if 'alexa' in command:
                        command = command.replace('alexa', '')
                        print(command)
            except:
                talk("I didn't understand. Please say it again")
            return command

        # function of getting api
        def wolfram(command):
            api_key = "TGEJGV-XGXWYWW26R"
            requester = wolframalpha.Client(api_key)
            requested = requester.query(command)

            try:
                Answer = next(requested.results).text
                return Answer

            except:
                talk("No data found")

        # function of run the AI
        def run_talking_robot():
            command = take_command()
            print(command)

            # playing video from YouTube
            if 'play' in command:
                song = command.replace('play', '')
                talk('playing ' + song)
                pywhatkit.playonyt(song)

            # current time
            elif 'current time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                talk('The current time is ' + time)

            # information of anything
            elif 'about' in command:
                person = command.replace('about', '')
                info = wikipedia.summary(person, 5)
                talk(info)

            # maker info
            elif 'who made you' in command:
                talk('Md. Fahmid Bin Mostafa made me')

            # information of this AI
            elif 'who are you' in command:
                say = '''Hey, I'm a virtual assistance.
                    Currently I don't have a name.
                    I live in Dhaka Bangladesh.
                    I have some emotion like smile and cry.
                    But I did not eat food as like a human.
                    You can ask me any question, I will try to give your questions answer properly.
                    If I doesn't able to give any question answer then I search it in google cause google is my big brother.
                    I love to give answer to your question.
                    My favorite food is electricity because I only eat electricity.'''


                talk(say)
            # how to
            elif 'how to' in command:
                how = command
                max_result = 1
                how_to = search_wikihow(how, max_result)
                assert len(how_to) == 1
                how_to[0].print()
                talk(how_to[0].summary)

            # Location
            elif 'where are you' in command:
                talk('I am now in ' + city + ", " + country)

            # jokes
            elif 'joke' in command:
                talk(pyjokes.get_joke())

            # favourite color of this AI
            elif 'your favourite colour' in command:
                talk("Red is my favourite colour")

            # marital info of this AI
            elif 'will you marry me' in command:
                talk("I am a virtual assistance and I can't marry with a human. Please don't mind.")

            # favourite food of this AI
            elif 'favourite food' in command:
                talk("I only eat electricity.")
            elif 'say' in command or 'speak' in command:
                says = command.replace('say', '')
                talk(says)
            # favourite movie of this AI
            elif 'favourite movie' in command:
                talk("Hawa is my favourite movie")

            # search anything
            elif 'search' in command:
                searches = command.replace('search', '')
                talk('Ok I am going to search ' + searches)
                pywhatkit.search(searches)
                wikipedia.summary(searches, 1)

            # current date
            elif 'date' in command:
                today = date.today()
                talk(today)

            # temperature know
            elif 'temperature' in command:
                search = command
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, 'html.parser')
                temperature = data.find("div",class_="BNeawe").text
                talk(f"{search} is now{temperature} celsius")

            # smile
            elif 'smile' in command:
                playsound.playsound('smile.mp3')

            # translate
            elif 'translate' in command:
                text = command.replace('translate into', '')


            # 1 line definition of anything
            elif 'what is' in command:
                person = command.replace('what is', '')
                info = wikipedia.summary(person, 1)
                talk(info)

            elif 'gmail' in command:
                webbrowser.open('https://mail.google.com/')

            elif 'google translate' in command:
                webbrowser.open('https://translate.google.com/')

            elif 'diu website' in command:
                webbrowser.open('https://daffodilvarsity.edu.bd/')

            elif 'diu notice' in command:
                webbrowser.open('https://daffodilvarsity.edu.bd/noticeboard')

            elif 'my department notice' in command:
                webbrowser.open('https://daffodilvarsity.edu.bd/department/cse/notice')

            elif 'my department website' in command:
                webbrowser.open('https://daffodilvarsity.edu.bd/department/cse/')

            elif 'portal' in command:
                webbrowser.open('http://studentportal.diu.edu.bd/')
            # lock the window
            elif 'lock' in command:
                pyautogui.keyDown('win')
                pyautogui.press('l')
                pyautogui.keyUp('win')

            # check internet speed
            elif 'internet speed' in command:
                talk("Wait a few second, I'm checking internet speed")
                st = speedtest.Speedtest()
                dl = st.download()
                down = dl / 1000000
                ul = st.upload()
                upload = ul / 1000000
                talk(f"Internet upload speed is {int(down)} Mbps and download speed is {int(upload)}Mbps")

            # song open in YouTube
            elif 'sing a song' in command:
                singing = random.choice(songs)
                pywhatkit.playonyt(singing)

            # greeting
            elif 'hello' in command:
                ans = random.choice(rand)
                talk(ans)

            # open software
            elif 'open' in command:
                app = command.replace('open', '')
                pyautogui.press('super')
                pyautogui.sleep(1)
                pyautogui.typewrite(app)
                pyautogui.sleep(2)
                pyautogui.press('enter')

            # close software
            elif 'close' in command:
                apps = command.replace('close', '')
                keyboard.press_and_release('alt + f4')
                keyboard.press_and_release('enter')


            # welcomed
            elif 'thank' in command:
                wlcm = random.choice(cong)
                talk(wlcm)

            # cry
            elif 'cry' in command:
                playsound.playsound('cry.mp3')

            # take screenshot
            elif 'take a screenshot' in command:
                img = pyautogui.screenshot()
                file = 'SAVE' + '.png'
                path = 'C:\\Users\\Hp\\Desktop\\ScreenShot\\' + file
                img.save(path)
            # answer of salam
            elif 'assalamu alaikum' in command:
                talk('walaikum assalam')

            # stop work of AI
            elif 'stop' in command:
                # talk("bye bye see you will again")
                talk("Ta ta, good bye")
                exit()

            # how are you
            elif 'how are you' in command:
                talk("I am fine, And what about you, sir?")
                command = take_command()
                if 'fine' in command:
                    talk("So you have a nice day today")

            # toss coin
            elif 'toss' in command:
                lst = ['head', 'tail']
                talk("Please choose head or tail")
                command = take_command()
                res = random.choice(lst)
                print(res, command)
                if res in command:
                    talk("You have won the toss")
                else:
                    talk("Sorry! You loss the toss")

            # open mobile camera
            elif "on mobile camera" in command:
                url = "http://192.168.0.102:8080/shot.jpg"
                while True:
                    img_arr = np.array(bytearray(urllib.request.urlopen(url).read()), dtype=np.uint8)
                    img = cv2.imdecode(img_arr, -1)
                    cv2.imshow('Camera', img)
                    q = cv2.waitKey(1)
                    if q == ord('q'):
                        break
                cv2.destroyAllWindows()

            # open mobile camera
            elif "your camera" in command:
                cap = cv2.VideoCapture(0)
                while True:
                    _, img = cap.read()
                    cv2.imshow('Camera', img)
                    q = cv2.waitKey(1)
                    if q == ord('q'):
                        break

            # calculation
            elif 'calculations' in command:
                try:
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        talk("Please tell me what you want to calculate, example 7+87")
                        print("Listening...")
                        audio = r.listen(source)
                    my_string = r.recognize_google(audio)
                except:
                    pass

                def get_operator_fn(op):
                    return {
                        '+': operator.add,
                        '-': operator.sub,
                        'x': operator.mul,
                        '/': operator.__truediv__,
                    }[op]

                def eval_binary_expression(op1, oper, op2):
                    op1, op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)

                talk("Your result is ")
                talk(eval_binary_expression(*(my_string.split())))

            # raise volume
            elif 'volume up' in command:
                pyautogui.press("volumeup")

            # down volume
            elif 'volume down' in command:
                pyautogui.press("volumedown")

            # mute volume
            elif 'mute volume' in command:
                pyautogui.press("volumemute")

            # check battery percentage

            elif 'battery percentage' in command:
                battery = psutil.sensors_battery()
                percent = battery.percent
                time = battery.secsleft
                time_delta = datetime.timedelta(seconds=time)
                hours, remainder = divmod(time_delta.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                if  20 < percent <= 50:

                    talk(f"This device has {percent} percent battery and time left {hours:02d}:{minutes:02d}:{seconds:02d}. You need to charge this device.")
                elif 10 < percent <= 20:
                    talk(f"This device has {percent} percent battery and time left {hours:02d}:{minutes:02d}:{seconds:02d}. You need to quickly charge this device.")
                elif 10 < percent <= 10:
                    talk(f"This device has {percent} percent battery and time left {hours:02d}:{minutes:02d}:{seconds:02d}. You need to quickly charge this device and stop use .")

            else:
                talk('I did not get it but I am going to search it for you')
                # pywhatkit.search(command)

        # Add the label and button to the GUI


        BtnShow = Button(self.root, text='Speak', font=("times new roman", 12, "bold"), width=23, bg='blue',
                         fg='white',
                         command=run_talking_robot)
        BtnShow.pack(expand=True)

        Btn = Button(self.root, text='Stop', font=("times new roman", 12, "bold"), command=stop_speaking)
        Btn.pack(expand=True)


if __name__ == "__main__":
    root = Tk()
    obj = AssistanceMama(root)
    root.mainloop()
