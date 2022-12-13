import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import time
import random

class Game():
    def __init__(self):
        root.geometry("1280x720")
        root.configure(bg='green')
        self.getImg()
        self.getObj("Nut", 5000)
        self.placeObj()
        self.monButt()
        self.getButt()
        self.placeButt()

    def ranNum(self):
        return random.randint(1, 6)

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
        self.name = Label(text=str(name), font=("Arial",18,""), width=25)
        self.money = Label(text=str(money), font=("Arial",18,""), width=25)
        self.monPay = Entry(width = 23, font=("Arial", 15, ""), justify='center')

    def getImg(self):
        img = Image.open("image\hiro.jpg")
        weight, height = img.size
        weight, height = int(weight*0.24), int(height*0.24)

        img = img.resize((weight, height))
        img = ImageTk.PhotoImage(img)

        self.label1 = tkinter.Label(image=img, bd=0)
        self.label1.image = img

        img = Image.open("image\lid.jpg")
        weight, height = img.size
        weight, height = int(weight*0.45), int(height*0.45)

        img = img.resize((weight, height))
        img = ImageTk.PhotoImage(img)

        self.label2 = tkinter.Label(image=img, bd=0)
        self.label2.image = img

    def placeObj(self):
        self.label1.place(relx=0.905, rely=0.89, anchor='center')
        self.label2.place(relx=0.9, rely=0.2, anchor='center')
        self.name.place(relx=0.9, rely=0.4, anchor='center')
        self.money.place(relx=0.9, rely=0.5, anchor='center')
        self.monPay.place(relx=0.91, rely=0.6, anchor='center')

    def monButt(self):
        self.mon15 = " "
        self.mon16 = " "
        self.mon25 = " "
        self.mon123 = " "
        self.mon5Low = " "
        self.mon1 = " "
        self.mon2 = " "
        self.mon36 = " "
        self.mon11Hiro = " "
        self.monLow = " "
        self.mon3 = " "
        self.mon24 = " "
        self.monHigh = " "
        self.mon4 = " "
        self.mon35 = " "
        self.mon6Low = " "
        self.mon6 = " "
        self.mon5 = " "
        self.mon41 = " "
        self.mon62 = " "
        self.mon61 = " "
        self.mon52 = " "
        self.mon456 = " "

    def getButt(self):
        self.butt15 = Button(text="1 o 5\n\n%s" %(self.mon15), command=lambda: self.playGame([1, 5]), font=("Arial",20,""), height=5, width=10, bd=5)
        self.butt16 = Button(text="1 o 6\n\n%s" %(self.mon16), command=lambda: self.playGame([1, 6]), font=("Arial",20,""), height=5, width=10, bd=5)
        self.butt25 = Button(text="2 o 5\n\n%s" %(self.mon25), command=lambda: self.playGame([2, 5]), font=("Arial",20,""), height=5, width=10, bd=5)
        self.butt123 = Button(text="1 o 2 o 3\n\n%s" %(self.mon123), command=lambda: self.playGame([1, 2, 3]), font=("Arial",20,""), height=5, width=10, bd=5)
        self.butt5low = Button(text="5 LOW\n\n%s" %(self.mon5Low), command=lambda: self.playGame([5, "LOW"]), font=("Arial",20,""), height=5, width=10, bd=5)
        self.butt1 = Button(text="1\n\n%s" %(self.mon1), command=lambda: self.playGame(1), font=("Arial",20,""), fg='red', height=5, width=10, bd=5)
        self.butt2 = Button(text="2\n\n%s" %(self.mon2), command=lambda: self.playGame(2), font=("Arial",20,""), height=5, width=10, bd=5)
        self.butt36 = Button(text="3 o 6\n\n%s" %(self.mon36), command=lambda: self.playGame([3, 6]), font=("Arial",20,""), height=5, width=10, bd=5)
        self.butt11Hiro = Button(text="11Hiro\n\n%s" %(self.mon11Hiro), command=lambda: self.playGame("11HILO"), font=("Arial",20,""), fg='red', height=5, width=21, bd=5)
        self.buttLow = Button(text="LOW\n\n%s" %(self.monLow), command=lambda: self.playGame("LOW"), font=("Arial",20,""), fg='red', height=5, width=10, bd=5)
        self.butt3 = Button(text="3\n\n%s" %(self.mon3), command=lambda: self.playGame(3), font=("Arial",20,""), height=5, width=10, bd=5)
        self.butt24 = Button(text="2 o 4\n\n%s" %(self.mon24), command=lambda: self.playGame([2, 4]), font=("Arial",20,""), height=5, width=10, bd=5)
        self.buttHigh = Button(text="HIGH\n\n%s" %(self.monHigh), command=lambda: self.playGame("HIGH"), font=("Arial",20,""), height=5, width=10, bd=5)
        self.butt4 = Button(text="4\n\n%s" %(self.mon4), command=lambda: self.playGame(4), font=("Arial",20,""), fg='red', height=5, width=10, bd=5)
        self.butt35 = Button(text="3 o 5\n\n%s" %(self.mon35), command=lambda: self.playGame([3, 5]), font=("Arial",20,""), height=5, width=10, bd=5)
        self.butt6low = Button(text="6 LOW\n\n%s" %(self.mon6Low), command=lambda: self.playGame([6, "LOW"]), font=("Arial",20,""), height=5, width=10, bd=5)
        self.butt6 = Button(text="6\n\n%s" %(self.mon6), command=lambda: self.playGame(6), font=("Arial",20,""), height=5, width=10, bd=5)
        self.butt5 = Button(text="5\n\n%s" %(self.mon5), command=lambda: self.playGame(5), font=("Arial",20,""), height=5, width=10, bd=5)
        self.butt41 = Button(text="4 o 1\n\n%s" %(self.mon41), command=lambda: self.playGame([4, 1]), font=("Arial",20,""), height=5, width=10, bd=5)
        self.butt62 = Button(text="6 o 2\n\n%s" %(self.mon62), command=lambda: self.playGame([6, 2]), font=("Arial",20,""), height=5, width=10, bd=5)
        self.butt61 = Button(text="6 o 1\n\n%s" %(self.mon61), command=lambda: self.playGame([6, 1]), font=("Arial",20,""), height=5, width=10, bd=5)
        self.butt52 = Button(text="5 o 2\n\n%s" %(self.mon52), command=lambda: self.playGame([5, 2]), font=("Arial",20,""), height=5, width=10, bd=5)
        self.butt456 = Button(text="4 o 5 o 6\n\n%s" %(self.mon456), command=lambda: self.playGame([4, 5, 6]), font=("Arial",20,""), height=5, width=10, bd=5)

    def placeButt(self):
        self.butt15.place(relx=0, rely=0, anchor='nw')
        self.butt16.place(relx=0, rely=0.25, anchor='nw')
        self.butt25.place(relx=0, rely=0.5, anchor='nw')
        self.butt123.place(relx=0, rely=0.75, anchor='nw')
        self.butt5low.place(relx=0.135, rely=0, anchor='nw')
        self.butt1.place(relx=0.135, rely=0.25, anchor='nw')
        self.butt2.place(relx=0.135, rely=0.5, anchor='nw')
        self.butt36.place(relx=0.135, rely=0.75, anchor='nw')
        self.butt11Hiro.place(relx=0.27, rely=0, anchor='nw')
        self.buttLow.place(relx=0.27, rely=0.25, anchor='nw')
        self.butt3.place(relx=0.27, rely=0.5, anchor='nw')
        self.butt24.place(relx=0.27, rely=0.75, anchor='nw')
        self.buttHigh.place(relx=0.405, rely=0.25, anchor='nw')
        self.butt4.place(relx=0.405, rely=0.5, anchor='nw')
        self.butt35.place(relx=0.405, rely=0.75, anchor='nw')
        self.butt6low.place(relx=0.540, rely=0, anchor='nw')
        self.butt6.place(relx=0.540, rely=0.25, anchor='nw')
        self.butt5.place(relx=0.540, rely=0.5, anchor='nw')
        self.butt41.place(relx=0.540, rely=0.75, anchor='nw')
        self.butt62.place(relx=0.675, rely=0, anchor='nw')
        self.butt61.place(relx=0.675, rely=0.25, anchor='nw')
        self.butt52.place(relx=0.675, rely=0.5, anchor='nw')
        self.butt456.place(relx=0.675, rely=0.75, anchor='nw')

root = Tk()
root.title("Hiro")
root.resizable(False, False)

Game()
root.mainloop()
