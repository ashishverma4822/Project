from tkinter import*
from tkinter import ttk,messagebox
import googletrans
import textblob
from langdetect import detect

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
root.mainloop()
