from tkinter import *
import pynput
from time import sleep

keyboard = pynput.keyboard.Controller()

root = Tk()
root.title("spa><er")
root.minsize(600, 600)

# main exec


def mainspam():
    sleep(5)
    for i in range(int(rep.get())):
        keyboard.type(keyword.get())
        keyboard.press(pynput.keyboard.Key.enter)
        keyboard.release(pynput.keyboard.Key.enter)

# title banner


# textbox for keyword

labelWord = Label(root, text="keyword : ")
labelWord.place(relx=0.3, rely=0.3)
keyword = Entry(root)
keyword.place(relx=0.4, rely=0.3)

# textbox for rep


labelRep = Label(root, text="Amount : ")
labelRep.place(relx=0.3, rely=0.4)
rep = Entry(root)
rep.place(relx=0.4, rely=0.4)

# button to exec


execute = Button(root, width=40, height=5, text="Click Me to Execute!", command=mainspam, fg="grey", bg="white")
execute.place(relx=0.26, rely=0.5)
warning = Label(root, text="Please Wait 5 Second's After you Pressed the Button", font=("times", 10))
warning.place(relx=0.26, rely=0.7)

root.mainloop()