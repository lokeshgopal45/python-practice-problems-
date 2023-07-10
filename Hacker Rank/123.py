from tkinter import *

main=Tk()

def lb():
    name=user.get()
    helo="HELLO"+" "+name+"!"
    if name !='':
        text.config(text=helo)
        user.delete(0,END)

user = Entry(main, widt=20, font=("k",20))
user.pack(padx=20, pady=20)

text = Label(main, text="ENTER YOUR NAME", font=("j", 20))
text.pack(padx=20)

btn = Button(main, text="say hello", font=("j", 20), command=lb)
btn.pack(padx=20, pady=30)

mainloop()
