import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import time
import random

class Game():
    def __init__(self):
        root.geometry("1280x720")
        root.configure(bg='green')
        self.getImg()
        self.getObj("Nut", 5000)
        self.time = Label(text="20", font=("Arial",18,""))
        self.time.place(relx=0.88, rely=0.35)
        self.placeObj()

    def ranNum(self):
        return random.randint(1, 6)

    def countdown(self):
        limit = 20
        while limit>-1:
            timer = '{:02d}'.format(limit)
            root.update()
            if limit > 3:
                self.time = Label(text=str(timer), font=("Arial",18,""))
            else:
                self.time = Label(text=str(timer), font=("Arial",18,""), fg='red')
            self.time.place(relx=0.88, rely=0.35)
            time.sleep(1)
            limit -= 1

    def openDice(self):
        self.label2.destroy()
        self.placeDice()

    def getDice(self, ran):
        print(ran)
        if ran == 1:
            self.img = Image.open("dice1.jpg")
        elif ran == 2:
            self.img = Image.open("dice2.jpg")
        elif ran == 3:
            self.img = Image.open("dice3.jpg")
        elif ran == 4:
            self.img = Image.open("dice4.jpg")
        elif ran == 5:
            self.img = Image.open("dice5.jpg")
        elif ran == 6:
            self.img = Image.open("dice6.jpg")
        weight, height = self.img.size
        weight, height = int(weight*0.07), int(height*0.07)

        self.img = self.img.resize((weight, height))
        self.img = ImageTk.PhotoImage(self.img)

    def placeDice(self):
        self.ran1 = self.ranNum()
        self.getDice(self.ran1)
        self.dice1 = tkinter.Label(image=self.img)
        self.dice1.image = self.img
        self.dice1.place(relx=0.87, rely=0.15, anchor='center')

        self.ran2 = self.ranNum()
        self.getDice(self.ran2)
        self.dice2 = tkinter.Label(image=self.img)
        self.dice2.image = self.img
        self.dice2.place(relx=0.92, rely=0.15, anchor='center')

        self.ran3 = self.ranNum()
        self.getDice(self.ran3)
        self.dice3 = tkinter.Label(image=self.img)
        self.dice3.image = self.img
        self.dice3.place(relx=0.89, rely=0.25, anchor='center')

    def shake(self):
        self.label2.place(relx=0.9, rely=0.15, anchor='center')
        root.update()
        time.sleep(1)
        self.label2.place(relx=0.9, rely=0.2, anchor='center')
        self.countdown()
        self.openDice()

    def getObj(self, name, money):
        self.name = Label(text=str(name), font=("Arial",18,""))
        self.money = Label(text=str(money), font=("Arial",18,""))

    def getImg(self):
        img = Image.open("hiro.jpg")
        weight, height = img.size
        weight, height = int(weight*1), int(height*1)

        img = img.resize((weight, height))
        img = ImageTk.PhotoImage(img)

        self.label1 = tkinter.Label(image=img)
        self.label1.image = img

        img = Image.open("lid.jpg")
        weight, height = img.size
        weight, height = int(weight*0.2), int(height*0.2)

        img = img.resize((weight, height))
        img = ImageTk.PhotoImage(img)

        self.label2 = tkinter.Label(image=img)
        self.label2.image = img

    def placeObj(self):
        btn = Button(text="Start", command=self.shake).place(relx=0.9, rely=0.8)
        self.label1.place(relx=0, rely=0)
        self.label2.place(relx=0.9, rely=0.2, anchor='center')
        self.name.place(relx=0.9, rely=0.5, anchor='center')
        self.money.place(relx=0.9, rely=0.55, anchor='center')

root = Tk()
root.title("Hiro")
root.resizable(False, False)

Game()
root.mainloop()
