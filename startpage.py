import tkinter
from tkinter import *
from PIL import Image, ImageTk
import os

class PageOne():
    def __init__(self):
        self.getImg()
        self.getBut()
        self.placeObj()

    def getImg(self):
        img = Image.open("hiroLogo.jpg")
        weight, height = img.size
        weight, height = int(weight*0.5), int(height*0.5)

        img = img.resize((weight, height))
        img = ImageTk.PhotoImage(img)

        self.label = tkinter.Label(image=img)
        self.label.image = img

    def getBut(self):
        self.btn_st = Button(text="Start", font=("Arial", 10, "bold"), width=30, height=2, activebackground="green", bd=5, command=self.callPageTwo, bg='#73c088')
        self.btn_qu = Button(text="Quit", font=("Arial", 10, "bold"), width=30, height=2, activebackground="red", bd=5, command=self.exitProgram, bg='#fd464a')

    def callPageTwo(self):
        self.clearObj()
        PageTwo()

    def placeObj(self):
        self.label.place(relx = 0.5, rely = 0.4, anchor = "center")
        self.btn_st.place(relx = 0.5, rely = 0.8, anchor = "center")
        self.btn_qu.place(relx = 0.5, rely = 0.9, anchor = "center")

    def clearObj(self):
        self.label.destroy()
        self.btn_st.destroy()
        self.btn_qu.destroy()

    def exitProgram(self):
        os._exit(0)


#One Person
class PageTwo():
    def __init__(self):
        self.check = False
        self.getObj()
        self.placeObj()

    def getObj(self):
        self.label1 = Label(text="Name", font=("Arial", 13, "bold"))
        self.entPla = Entry(width = 20, font=("Arial", 15, ""), justify='center')
        self.label2 = Label(text="How Much Money To Play", font=("Arial", 13, "bold"))
        self.entMon = Entry(width = 20, font=("Arial", 15, ""), justify='center')
        self.btn = Button(text="Enter", font=("Arial", 10, "bold"), command=self.getValue, bd=5, bg='#73c088')

    def placeObj(self):
        self.label1.place(relx = 0.5, rely = 0.35, anchor = "center")
        self.entPla.place(relx = 0.5, rely = 0.4, anchor = "center")
        self.label2.place(relx = 0.5, rely = 0.48, anchor = "center")
        self.entMon.place(relx = 0.5, rely = 0.53, anchor = "center")
        self.btn.place(relx = 0.5, rely = 0.63, anchor = "center")

    def getValue(self):
        self.namePla = self.entPla.get()
        self.numMon = self.entMon.get()
        self.clearObj()
        Game()

    def clearObj(self):
        self.label1.destroy()
        self.label2.destroy()
        self.entPla.destroy()
        self.entMon.destroy()
        self.btn.destroy()

    #     if self.numMon.isnumeric() == False or self.numPla.isnumeric() == False or int(self.numPla) > 4 or int(self.numPla) < 1:
    #         self.error()
    #     else:
    #         print(self.numMon, self.numPla)

    # def error(self):
    #     self.check = True
    #     self.placeObj()

class Game():
    def __init__(self):
        root.geometry("1280x720")
        self.getImg()
        self.placeObj()

    def getImg(self):
        img = Image.open("hiro.jpg")
        weight, height = img.size
        weight, height = int(weight*1), int(height*1)

        img = img.resize((weight, height))
        img = ImageTk.PhotoImage(img)

        self.label = tkinter.Label(image=img)
        self.label.image = img

    def placeObj(self):
        self.label.place(relx=0, rely=0)

root = Tk()
root.title("Hiro")
root.geometry("720x576")
root.resizable(False, False)

pageOne = PageOne()
root.mainloop()
