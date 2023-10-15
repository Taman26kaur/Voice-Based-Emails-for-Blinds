from tkinter.font import BOLD
import speech_recognition as sr
import easyimap as e
import pyttsx3 
import smtplib
import os
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import subprocess


unm = os.environ.get('EMAIL_USER')
pwd = os.environ.get('EMAIL_PASS')


t_count = 0

def line_counter(str,text_area):
    global t_count
    t_count+= 1
    str_counter = f"{t_count}" + ".0"
    text_area.insert(str_counter,str+"\n")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 
engine.setProperty('rate', 150) 

def speak(str):
    engine.say(str)         
    engine.runAndWait()

r = sr.Recognizer()
def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        str = "Speak Now: "
        speak(str)
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)    #google web speech API
            return text
        except:
            str = "Sorry, not able to recognize..."
            speak(str)

def remove(string):
    return string.replace(" ", "")

def sendmail():
    subprocess.call(['python', r'C:\Users\taman\Desktop\Group2_Code\sendmail_gui.py'])

def readmail():
    subprocess.call(['python', r'C:\Users\taman\Desktop\Group2_Code\readmail_gui.py'])


def main_function():
    
    str = "Hello, Welcome. I am voice based assistance for your emails."
    line_counter(str,text_area)
    root.update()
    speak(str)

    str = "What do you want to do?"
    line_counter(str,text_area)
    root.update()
    speak(str)
   
    str_1 = "Speak SEND to send email"
    str_2 = "Speak READ to read mail"
    str_3 = "Speak EXIT to exit menu"
    while(1):

        line_counter(str_1,text_area)
        line_counter(str_2,text_area)
        line_counter(str_3,text_area)

        root.update()
        speak(str_1)
        speak(str_2)
        speak(str_3)

        ch = listen()

        if (ch == "send" or ch == "one" ):

            str = "You have chosen to send."
            line_counter(str,text_area)
            root.update()
            speak(str)
            sendmail()

        elif (ch == 'read' or ch == "two"):   
            str = "You have choosen to read email."
            line_counter(str,text_area)
            root.update()
            speak(str)
            readmail()

        elif (ch == 'exit' or ch == "three"):
            str = "Thank you for using."
            line_counter(str,text_area)
            root.update()
            speak(str)
            exit(1)

        else:
            str = "Please say your choice again."
            line_counter(str,text_area)
            root.update()
            speak(str)

root = tk.Tk()
root.title("Voice based email system")
root.state("zoomed")
root.grid_rowconfigure(0, weight = 1) 
root.grid_columnconfigure(0, weight = 1) 


mypic=Image.open('MainMenu.png')
resized=mypic.resize((1500,770))
newpic=ImageTk.PhotoImage(resized)
button= Button(root, image= newpic ,command= main_function,borderwidth=0)
button.pack(pady=10)

sendimg = Image.open(r'C:\Users\taman\Desktop\Group2_Code\send.png')
sendimg_p = ImageTk.PhotoImage(sendimg.resize((160,160)))
sendbutton = tk.Button(root,image = sendimg_p ,command = sendmail, bd=0 , bg='pink',activebackground='white')
sendbutton.place(x = 1200, y = 100)
sendbutton_label = tk.Label(root,text = "Send E-mail", fg="white",bg='gray51',font=('Ar cena', 14,BOLD))
sendbutton_label.place(x=1220, y=290)

readimg = Image.open(r'C:\Users\taman\Desktop\Group2_Code\read.png')
readimg_p = ImageTk.PhotoImage(readimg.resize((160,160)))
readbutton = tk.Button(root,image = readimg_p ,command = readmail, bd=0 , bg='pink',activebackground='white')
readbutton.place(x = 1200, y = 400)
readbutton_label = tk.Label(root,text = "Read E-mail",fg="white",bg='gray51',font=('Ar cena', 14,BOLD))
readbutton_label.place(x=1220, y=590)

text_area = tk.Text(root,height = 20,width = 70,font = ("Ar cena",12),bd = 3,fg='white',bg='light sea green')
text_area.place(x = 200, y = 310)

startimg = Image.open(r'C:\Users\taman\Desktop\Group2_Code\start.png')
startimg_p = ImageTk.PhotoImage(startimg)
startbutton = tk.Button(root,image = startimg_p,command = main_function , bd =0, bg='white',activebackground='white')
startbutton.place(x = 765, y = 315)

root.mainloop()

 