# took testing as the main project

import random
import string


import pyperclip
from tkinter import *

def clear():
    length_box.delete(0)
def generator():
    samllalpha=string.ascii_lowercase
    capitalalpha=string.ascii_uppercase
    letter=string.ascii_letters
    digits=string.digits
    special=string.punctuation

    combine=samllalpha+capitalalpha+digits+special

    length=int(length_box.get())
    if choice.get()==1:
        passwordfield.insert(0,random.sample(letter,length))
    if choice.get()==2:
        passwordfield.insert(0,random.sample(letter+digits,length))
    if choice.get()==3:
        passwordfield.insert(0,random.sample(combine,length))
    clear()
    length_box.insert(0,0)
    # fpass=random.sample(combine,length)
    # passwordfield.insert(0,fpass)

def copy():
    temp=passwordfield.get()
    pyperclip.copy(temp)





def reset():
    passwordfield.delete(0,'end')

root=Tk()
root.title("Password_Generator")
root.geometry("280x300")
root.resizable(False,False)
root.config(bg="lime")
choice=IntVar()
Font=('arial',13,'bold')

passwordLabel=Label(root,text='Password Generator',font=('times new roman',20,'bold'),bg='black',fg='white')
passwordLabel.grid(pady=10,padx=20)
weekradio=Radiobutton(root,text="Week",value=1,variable=choice,font=Font)
#weekradio.grid(pady=5)
weekradio.place(x=10,y=61,height=26,width=75)

mediumradio=Radiobutton(root,text="Medium",value=2,variable=choice,font=Font)
#mediumradio.grid(pady=5)
mediumradio.place(x=93,y=61,height=26,width=89)

strongradio=Radiobutton(root,text="Strong",value=3,variable=choice,font=Font)
#strongradio.grid(pady=5)
strongradio.place(x=190,y=61,height=26,width=80)



lengthLabel=Label(root,text='Password Length',font=Font,bg='black',fg='white')
#lengthLabel.grid(pady=25)
lengthLabel.place(x=68,y=100)


length_box=Spinbox(root,from_=5,to=32,width=5,font=('arial',13,'bold'))
#length_box.grid(pady=35)
length_box.place(x=105,y=137,width=70)





generateButton=Button(root,text="Generate",font=Font, command=generator)
#generateButton.grid(pady=90)
generateButton.place(x=96,y=170,width=90)


passwordfield=Entry(root,width=25,bd=2,font=Font)
#passwordfield.grid(pady=5)
passwordfield.place(x=20,y=210)


copyButton=Button(root,text="Copy",font=Font,command=copy)
#copyButton.grid(pady=5)
copyButton.place(x=40,y=245)


resetButton=Button(root,text="Reset",font=Font, command=reset)
#copyButton.grid(pady=5)
resetButton.place(x=170,y=245)



root.mainloop()
