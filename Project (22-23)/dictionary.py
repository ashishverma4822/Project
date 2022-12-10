from sys import builtin_module_names
from tkinter import*
from PyDictionary import PyDictionary

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

root.mainloop()