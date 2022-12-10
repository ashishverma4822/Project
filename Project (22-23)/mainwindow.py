import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import ttk,messagebox
import googletrans
import textblob
from langdetect import detect
from tkinter import filedialog
from tkinter.ttk import Combobox 
from gtts import gTTS
import pyttsx3
import speech_recognition as sr
from sys import builtin_module_names
from tkinter import*
from PyDictionary import PyDictionary
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


def Translator():
    root=Tk()
    root.title('Translater')
    root.geometry("900x450+200+200")
    root.resizable(False, False)

    #image_icon=PhotoImage(file='icon.png')
    #root.iconphoto(False,image_icon)

    #arrow_image=PhotoImage(file='arrow.png')
    #arrow_image=arrow_image.subsample(9,9)
    def label_change():
        c=combo1.get()
        c1=combo2.get()
        label1.configure(text=c)
        label2.configure(text=c1)
        root.after(1000,label_change)

    def translate_now():
        global language
        try:
            text_= text1.get(1.0,END)
            c2=combo1.get()
            c3=combo2.get()
            print("Text: ",text_)
            if(text_):
                words=textblob.TextBlob(text_)
                lan = c2[0] + c2[1]
                print("Lan: ",lan)
                lan_ = c3[0] + c3[1]
                words=words.translate(from_lang=lan,to=str(lan_))
                text2.delete(1.0,END)
                text2.insert(END,words)
        except Exception as e:        
            messagebox.showerror('translater','Please try again')
    language= googletrans.LANGUAGES
    language_=list(language.values())
    lang1=language.keys()
    combo1=ttk.Combobox(root,values=language_,font='times 10 bold',state='r')
    combo1.place(x=120,y=20)
    combo1.set('english')

    label1=Label(root,text='english',font='segeo 30 bold',bg='#43A6C6',width=17,relief=GROOVE)
    label1.place(x=0,y=50)

    f=Frame(root,bg='#1E5162',bd=5)
    f.place(x=14,y=118,width=380,height=220)

    text1=Text(f,font='times 20 bold',bg='white',relief=GROOVE,wrap=WORD)
    text1.place(x=0,y=0,width=370,height=210)

    scroll_bar1=Scrollbar(f)
    scroll_bar1.pack(side='right',fill='y')
    scroll_bar1.configure(command=text1.yview)
    text1.configure(yscrollcommand=scroll_bar1.set)

    combo2=ttk.Combobox(root,values=language_,font='times 10 bold',state='r')
    combo2.place(x=600,y=20)
    combo2.set('english')

    label2=Label(root,text='english',font='segeo 30 bold',bg='#43A6C6',width=17,relief=GROOVE)
    label2.place(x=485,y=50)

    f1=Frame(root,bg='#1E5162',bd=5)
    f1.place(x=500,y=118,width=380,height=220)

    text2=Text(f1,font='times 20 bold',bg='white',relief=GROOVE,wrap=WORD,fg='green')
    text2.place(x=0,y=0,width=370,height=210)

    scroll_bar2=Scrollbar(f1)
    scroll_bar2.pack(side='right',fill='y')
    scroll_bar2.configure(command=text2.yview)
    text2.configure(yscrollcommand=scroll_bar2.set)

    #image_label=Label(root,image=arrow_image,width=150)
    #image_label.place(x=445,y=50)

    trans_btn = Button(root,text='Translate' , font='Imapct 15 bold italic', activebackground='#1E5162',curso='hand2' ,bd=5,bg='#43A6C6',fg='white',command=translate_now)
    trans_btn.place(x=390,y=350)
    label_change()
    root.configure(bg="#181818")


def Dictionary():
    dictionary = PyDictionary()
    root= Tk()
    root.title('Dictionary')
    root.geometry("900x450+200+200")
    root.resizable(False, False)
    root.configure(bg="#181818")

    def dict():
        meaning.config(text=dictionary.meaning(word.get())['Noun'][0])

    Label(root, text="Dictionary", font="Helvetica 20 bold", fg="Blue").pack(pady=10)

    frame=Frame(root)
    Label(frame,text="Type Word", font ="Helvetica 15 bold").pack(side=LEFT)
    word=Entry(frame,font="Helvetica 15 bold")
    word.pack()
    frame.pack(pady=10)

    frame1=Frame(root)
    Label(frame1,text="Meaning :-", font =("Helvetica 10 bold")).pack(side=LEFT)
    meaning=Label(frame1,text="",font="Helvetica 10 bold")
    meaning.pack()
    frame1.pack(pady=10)

    Button(root,text="Submit",font="Helvetica 15 bold",command=dict).pack()


texttospeechbutton = Button(root, text='Text-To-Speech Conversion', font=('Times New Roman', 16), bg='light blue', command=TextToSpeech)
texttospeechbutton.place(x=300, y=150)

speechtotextbutton = Button(root, text='Speech-To-Text Conversion', font=('Times New Roman', 16), bg='light blue', command=SpeechToText)
speechtotextbutton.place(x=300, y=200)

translatorbutton = Button(root,text=   '        Translator       ',font=('Times New Roman', 16), bg='light blue', command=Translator)
translatorbutton.place(x=330, y=250)

dictionarybutton = Button(root,text=   '        Dictionary      ',font=('Times New Roman', 16), bg='light blue', command=Dictionary)
dictionarybutton.place(x=330, y=300)

root.update()
root.mainloop()
