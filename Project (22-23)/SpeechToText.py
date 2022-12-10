import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import filedialog
from tkinter.ttk import Combobox 
from gtts import gTTS
import pyttsx3
import speech_recognition as sr
import os


root= Tk()
root.title('Text And Speech Tool')
root.geometry("900x450+200+200")
root.resizable(False, False)
root.configure(bg="#181818")

image_icon=PhotoImage(file="speak.png")
root.iconphoto(False,image_icon)

#Top Frame
Top_frame=Frame(root,bg="#282828",width=900,height=100)
Top_frame.place(x=0,y=0)

#Logo=PhotoImage(file="Logo")
#Label(Top_frame,image=Logo,bg="#282828").place(x=10,y=5)

Label(Top_frame,text="TEXT AND SPEECH TOOL" ,font="arial 20 bold",bg="#282828",fg="#3090C7").place(x=250,y=30)


def TextToSpeech():
    engine = pyttsx3.init()
    def speak():
        text=text_area.get(1.0,END)
        gender=gender_combobox.get()
        speed=speed_combobox.get()
        voices=engine.getProperty('voices')
    
        def setvoice():
            if(gender == 'Male'):
                engine.setProperty('voice',voices[0].id)
                engine.say(text)
                engine.runAndWait()
            else:
                engine.setProperty('voice',voices[1].id)
                engine.say(text)
                engine.runAndWait()
            
        if(text):
            if(speed =="Fast"):
                engine.setProperty('rate',250)
                setvoice()
            elif(speed=="Normal"):
                engine.setProperty('rate', 150)
                setvoice()
            else:
                engine.setProperty('rate', 60)
                setvoice()
                   
    def download():
        text=text_area.get(1.0,END)
        gender=gender_combobox.get()
        speed=speed_combobox.get()
        voices=engine.getProperty('voices')
    
        def setvoice():
            if(gender == 'Male'):
                engine.setProperty('voice',voices[0].id)
                path=filedialog.askdirectory()
                os.chdir(path)
                engine.save_to_file(text,'text.mp3')
                engine.runAndWait()
            else:
                engine.setProperty('voice',voices[1].id)
                path=filedialog.askdirectory()
                os.chdir(path)
                engine.save_to_file(text,'text.mp3')
                engine.runAndWait()
            
        if(text):
            if(speed =="Fast"):
                engine.setProperty('rate',250)
                setvoice()
            elif(speed=="Normal"):
                engine.setProperty('rate', 150)
                setvoice()
            else:
                engine.setProperty('rate', 60)
                setvoice()

    texttospeechwindow = Toplevel(root)
    texttospeechwindow.title("Text to Speech")
    texttospeechwindow.geometry("900x450+200+200")
    texttospeechwindow.resizable(False,False)
    texttospeechwindow.configure(bg="#181818")
    
    image_icon=PhotoImage(file="speak.png")
    texttospeechwindow.iconphoto(False,image_icon)

    #Top Frame
    Top_frame=Frame(texttospeechwindow,bg="#282828",width=900,height=100)
    Top_frame.place(x=0,y=0)

    #Logo=PhotoImage(file="Logo")
    #Labe1l(Top_frame,image=Logo,bg="#282828").place(x=10,y=5)

    Label(Top_frame,text="TEXT TO SPEECH" ,font="arial 20 bold",bg="#282828",fg="#3090C7").place(x=100,y=30)

    ########
    text_area=Text(texttospeechwindow,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
    text_area.place(x=10,y=150,width=500,height=250)

    Label(texttospeechwindow,text="VOICE",font="arial 15 bold",bg="#181818",fg="#305065").place(x=580,y=160)
    Label(texttospeechwindow,text="SPEED",font="arial 15 bold",bg="#181818",fg="#305065").place(x=760,y=160)

    gender_combobox=Combobox(texttospeechwindow,values=['Male','Female'],font="arial 14",state='r',width=10)
    gender_combobox.place(x=550,y=200)
    gender_combobox.set('Male')

    speed_combobox=Combobox(texttospeechwindow,values=['Fast','Normal','Slow'],font="arial 14",state='r',width=10)
    speed_combobox.place(x=730,y=200)
    speed_combobox.set('Normal')
    
    #imageicon=PhotoImage(file="speak.png")
    btn=Button(texttospeechwindow,text="Speak",width=10,font="arial 14 bold",command=speak)
    btn.place(x=550,y=280)
    
    #imageicon2=PhotoImage(file="speak.png")
    save=Button(texttospeechwindow,text="Save",width=10,bg="#39c790",font="arial 14 bold",command=download)
    save.place(x=730,y=280)

def SpeechToText():
    speechtotextwindow = Toplevel(root)
    speechtotextwindow.title('Speech-to-Text Converter')
    speechtotextwindow.geometry("900x450+200+200")
    speechtotextwindow.configure(bg='#181818')
    
    image_icon=PhotoImage(file="speak.png")
    speechtotextwindow.iconphoto(False,image_icon)

    #Top Frame
    Top_frame=Frame(speechtotextwindow,bg="#282828",width=900,height=100)
    Top_frame.place(x=0,y=0)

    #Logo=PhotoImage(file="Logo")
    #Labe1l(Top_frame,image=Logo,bg="#282828").place(x=10,y=5)

    Label(Top_frame,text="SPEECH TO TEXT" ,font="arial 20 bold",bg="#282828",fg="#3090C7").place(x=100,y=30)
    text1=''
    file_name=("D:/Project (22-23)/Speech.wav")
    def recordvoice():
        while True:
            text1 =''
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio=r.listen(source)
                try:    
                    text1 = r.recognize_google(audio)
                    print(text1)
                except:
                    pass
                return text1
    def Filevoice():
        while True:
            text1 =''
            r = sr.Recognizer()
            with sr.AudioFile(file_name) as source: # open file 
                audio=r.listen(source)
                try:    
                    text1 = r.recognize_google(audio)
                    print(text1)
                except:
                    pass
                return text1           
    def Reset():
        text.delete(1.0,END)            
 
    text = Text(speechtotextwindow, font=12, height=5, width=30)
    text.place(x=10,y=150,width=500,height=250)
   
    recordbutton = Button(speechtotextwindow,text="Record",width=10,bg="#39c790",font="arial 14 bold", command=lambda: text.insert(END, recordvoice()))
    recordbutton.place(x=550, y=200)

    filebutton = Button(speechtotextwindow, text='Import',width=10, bg='#39c790',font="arial 14 bold", command=lambda: text.insert(END, Filevoice()))
    filebutton.place(x=730, y=200)



texttospeechbutton = Button(root, text='Text-To-Speech Conversion', font=('Times New Roman', 16), bg='light blue', command=TextToSpeech)
texttospeechbutton.place(x=300, y=150)

speechtotextbutton = Button(root, text='Speech-To-Text Conversion', font=('Times New Roman', 16), bg='light blue', command=SpeechToText)
speechtotextbutton.place(x=300, y=200)

root.update()
root.mainloop()