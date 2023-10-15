import tkinter as tk
from tkinter.font import BOLD
from PIL import Image, ImageTk
import speech_recognition as sr
import easyimap as e
import pyttsx3 
import smtplib
import os
import time

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

def new_exit_function():
   
    choice ="yes"
    while(choice == "yes"):

        str = "Do you want to read another email or exit this module"
        line_counter(str,text_area)
        root.update()
        speak(str)

        str_1 = "Speak STAY to stay"
        str_2 = "Speak EXIT to exit"

        line_counter(str_1,text_area)
        line_counter(str_2,text_area)
        root.update()
        speak(str_1)
        speak(str_2)

        ch = listen()

        if (ch == "stay" or ch == "one" ):

            str = "You have chosen to stay."
            line_counter(str,text_area)
            root.update()
            speak(str)
            
            text_area.delete("1.0", "end")
            root.update()

            global t_count
            t_count = 0
            main_function()

        elif (ch == 'exit' or ch == "two"):   
            
            str = "You have choosen to exit"
            line_counter(str,text_area)
            root.update()
            speak(str)
            exit(1)
        
        else:
            str = "Please say your choice again."
            line_counter(str,text_area)
            root.update()
            speak(str)
            
def main_function():

    server = e.connect("imap.gmail.com", unm, pwd)
    server.listids()

    str = " Please say the serial number of the email you want to read starting from the latest"
    speak(str)

    a=listen()

    if(a=='one' or a=='1'):
        a=1
    elif(a=='tu' or a=='2' or a=='two'):
        a=3
    elif(a=='three' or a=='3'):
        a=3
    elif(a=='four' or a=='4' or a=='for'):
        a=4
    elif(a=='five' or a=='5'):
        a=5
    elif(a=='six' or a=='6'):
        a=6
    elif(a=='seven' or a=='7'):
        a=7
    elif(a=='eight' or a=='8'):
        a=8
    elif(a=='nine' or a=='9'):
        a=9
    elif(a=='ten' or a=='10'):
        a=10
    
    b= a - 1

    email = server.mail(server.listids()[b])

    str = "The email is from"
    speak(str)
    emailvar.set(email.from_addr)
    root.update()
    speak(email.from_addr)
    
    str = "The subject of the mail is"
    speak(str)
    subjectvar.set(email.title)
    root.update()
    speak(email.title)

    str = "The body of the mail is"
    speak(str)
    line_counter(email.body,text_area)
    root.update()
    speak(email.body)  

    time.sleep(2)
    new_exit_function()

    
root = tk.Tk()
root.title("Voice based email system")
root.state("zoomed")
root.grid_rowconfigure(0, weight = 1) 
root.grid_columnconfigure(0, weight = 1) 


mypic=Image.open('reading_mail.png')
resized=mypic.resize((1500,770))
newpic=ImageTk.PhotoImage(resized)
button= tk.Button(root, image= newpic ,command= main_function,borderwidth=0)
button.pack(pady=10)

emailvar = tk.StringVar()
subjectvar = tk.StringVar()

email_label = tk.Label(root,text = "EMAIL TITLE: ",  bd=0 , bg='white', font = ("Arial",12,BOLD)) 
email_label.place(x=480,y=300)
email_input = tk.Entry(root,width=100,bg="#fefefe" ,fg="black",textvariable=emailvar)
email_input.place(x=600,y=300)

subject_label = tk.Label(root,text = "SUBJECT : ",  bd=0 , bg='white', font = ("Arial",12,BOLD)) 
subject_label.place(x=480,y=350)
subject_input = tk.Entry(root,width=100,bg="#fefefe" ,fg="black",textvariable=subjectvar)
subject_input.place(x=600,y=350)

body_label = tk.Label(root,text = "EMAIL BODY : ",  bd=0 , bg='white', font = ("Arial",12,BOLD)) 
body_label.place(x=480,y=400)
text_area = tk.Text(root,height = 20,width = 105,font = ("Arial",9),bd = 3)
text_area.place(x = 480, y = 430)

root.mainloop()