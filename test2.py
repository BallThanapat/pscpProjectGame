import tkinter
from tkinter import *
from PIL import Image, ImageTk
import os

class App():
    def __init__(self):
        self.getImg()
        self.getBut()
        self.placeObj()

    def getImg(self):
        img = Image.open("hiro.jpg")
        weight, height = img.size
        weight, height = int(weight*1), int(height*1)

        img = img.resize((weight, height))
        img = ImageTk.PhotoImage(img)

        self.label = tkinter.Label(image=img)
        self.label.image = img

    def getBut(self):
        self.btn_st = Button(text="Start", width=30, height=2, activebackground="gray", bd=5)
        self.btn_qu = Button(text="Quit", width=30, height=2, activebackground="gray", bd=5, command=self.exitProgram)

    def placeObj(self):
        self.label.place(relx = 0.5, rely = 0.4, anchor = "center")
        self.btn_st.place(relx = 0.5, rely = 0.75, anchor = "center")
        self.btn_qu.place(relx = 0.5, rely = 0.85, anchor = "center")

    def exitProgram(self):
        os._exit(0)

root = Tk()
root.title("Hiro")
root.geometry("1024x720")
root.resizable(False, False)

app = App()
root.mainloop()
