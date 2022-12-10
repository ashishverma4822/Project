import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root=Tk()
root.title("Text to Speech")
root.geometry("900x450+200+200")
root.resizable(False,False)
root.configure(bg="#181818")
#icon 
image_icon=PhotoImage(file="speak.png")
root.iconphoto(False,image_icon)

#Top Frame
Top_frame=Frame(root,bg="#282828",width=900,height=100)
Top_frame.place(x=0,y=0)

#Logo=PhotoImage(file="Logo")
#Label(Top_frame,image=Logo,bg="#282828").place(x=10,y=5)

Label(Top_frame,text="TEXT TO SPEECH" ,font="arial 20 bold",bg="#282828",fg="#3090C7").place(x=100,y=30)

########
text_area=Text(root,font="RObote 20",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=150,width=500,height=250)

Label(root,text="VOICE",font="arial 15 bold",bg="#181818",fg="#305065").place(x=580,y=160)
Label(root,text="SPEED",font="arial 15 bold",bg="#181818",fg="#305065").place(x=760,y=160)

gender_combobox=Combobox(root,values=['Male','Female'],font="arial 14",state='r',width=10)
gender_combobox.place(x=550,y=200)
gender_combobox.set('Male')

speed_combobox=Combobox(root,values=['Fast','Normal','Slow'],font="arial 14",state='r',width=10)
speed_combobox.place(x=730,y=200)
speed_combobox.set('Normal')
btn=Button(root,text="Speak",width=10,font="arial 14 bold")
btn.place(x=550,y=280)

root.mainloop()
