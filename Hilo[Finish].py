import tkinter
from tkinter import *
from PIL import Image, ImageTk
import os
import time
import random

class PageOne():
    def __init__(self):
        root.geometry("720x576")
        root.configure(bg='white')
        self.getImg()
        self.getBut()
        self.placeObj()

    def getImg(self):
        img = Image.open("image\hiroLogo.jpg")
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
        self.label1 = Label(text="Name", font=("Arial", 15, ""))
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
        if self.numMon.isnumeric() and int(self.numMon) > 0:
            self.clearObj()
            Game(self.namePla, self.numMon)
        else:
            self.getObj()
            self.placeObj()
            Label(text="Input Must Be\nCardinal Numbers", fg='red', font=("Arial", 13, "")).place(relx = 0.75, rely = 0.53, anchor = "center")

    def clearObj(self):
        self.label1.destroy()
        self.label2.destroy()
        self.entPla.destroy()
        self.entMon.destroy()
        self.btn.destroy()

class Game():
    def __init__(self, name, money):
        root.geometry("1280x750")
        root.configure(bg='green')
        self.getObj(name, money)
        self.showScreen()
        self.label3 = False

    def playGame(self, id):
        moneyBet = self.monPay.get()
        if self.label3:
            self.label3.destroy()
        if moneyBet.isnumeric():
            moneyBet = int(self.monPay.get())
            if int(self.money['text'])-moneyBet >= 0:
                self.money['text'] = int(self.money['text'])-moneyBet
            elif int(self.money['text'])-moneyBet < 0:
                moneyBet = int(self.money['text'])
                self.money['text'] = 0
            self.keepNum(id, moneyBet)
        else:
            self.label3 = Label(text="Input Must Be\nCardinal Numbers", fg='red', font=("Arial", 13, ""), bg='green')
            self.label3.place(relx = 0.9, rely = 0.55, anchor = "center")

    def newGame(self):
        self.butt15.destroy()
        self.butt16.destroy()
        self.butt25.destroy()
        self.butt123.destroy()
        self.butt5low.destroy()
        self.butt1.destroy()
        self.butt2.destroy()
        self.butt36.destroy()
        self.butt11Hiro.destroy()
        self.buttLow.destroy()
        self.butt3.destroy()
        self.butt24.destroy()
        self.buttHigh.destroy()
        self.butt4.destroy()
        self.butt35.destroy()
        self.butt6low.destroy()
        self.butt6.destroy()
        self.butt5.destroy()
        self.butt41.destroy()
        self.butt62.destroy()
        self.butt61.destroy()
        self.butt52.destroy()
        self.butt456.destroy()
        self.open.destroy()
        self.label.destroy()
        self.label1.destroy()
        self.label2.destroy()
        self.btn.destroy()
        self.dice1img.destroy()
        self.dice2img.destroy()
        self.dice3img.destroy()
        self.name.destroy()
        self.money.destroy()
        self.monPay.destroy()
        self.btn2.destroy()
        self.label4.destroy()
        self.label5.destroy()
        if self.label3:
            self.label3.destroy()
        PageOne()

    def showScreen(self):
        if int(self.money['text']) <= 0:
            img = Image.open("image\lose.jpg")
            weight, height = img.size
            weight, height = int(weight*0.8), int(height*0.8)

            img = img.resize((weight, height))
            img = ImageTk.PhotoImage(img)
            self.label = tkinter.Label(image=img, bd=0)
            self.label.image = img
            self.label.place(relx=0.5, rely=0.5, anchor='center')

            self.btn = Button(text='New Game', bg='green', font=("Arial", 13, ""), width=10, command=lambda: self.newGame())
            self.btn.place(relx=0.5, rely=0.75, anchor='center')
        else:
            self.bet = []
            self.getImg()
            self.placeObj()
            self.monButt()
            self.getButt()
            self.placeButt()
            self.shake()

    def killObj(self):
        self.butt15.destroy()
        self.butt16.destroy()
        self.butt25.destroy()
        self.butt123.destroy()
        self.butt5low.destroy()
        self.butt1.destroy()
        self.butt2.destroy()
        self.butt36.destroy()
        self.butt11Hiro.destroy()
        self.buttLow.destroy()
        self.butt3.destroy()
        self.butt24.destroy()
        self.buttHigh.destroy()
        self.butt4.destroy()
        self.butt35.destroy()
        self.butt6low.destroy()
        self.butt6.destroy()
        self.butt5.destroy()
        self.butt41.destroy()
        self.butt62.destroy()
        self.butt61.destroy()
        self.butt52.destroy()
        self.butt456.destroy()
        self.btn2.destroy()
        self.label1.destroy()
        self.label4.destroy()
        self.label5.destroy()
        self.open.destroy()

    def checkList(self, id):
        if id not in self.bet:
            self.bet.append(id)
        print(self.bet)

    def ranNum(self):
        return random.randint(1, 6)

    def openDice(self):
        self.label2.destroy()
        self.placeDice()
        self.checkHiLo()
        self.plusMoney()
        self.disButt()
        self.btn2 = Button(text="Next Bet", command=lambda: self.removeDice(), font=("Arial", 18, ""), height=2, width=8, bd=5)
        self.btn2.place(relx=0.9, rely=0.7, anchor='center')

    def removeDice(self):
        self.dice1img.destroy()
        self.dice2img.destroy()
        self.dice3img.destroy()
        self.killObj()
        self.showScreen()

    def disButt(self):
        self.butt15['state'] = "disabled"
        self.butt16['state'] = "disabled"
        self.butt25['state'] = "disabled"
        self.butt123['state'] = "disabled"
        self.butt5low['state'] = "disabled"
        self.butt1['state'] = "disabled"
        self.butt2['state'] = "disabled"
        self.butt36['state'] = "disabled"
        self.butt11Hiro['state'] = "disabled"
        self.buttLow['state'] = "disabled"
        self.butt3['state'] = "disabled"
        self.butt24['state'] = "disabled"
        self.buttHigh['state'] = "disabled"
        self.butt4['state'] = "disabled"
        self.butt35['state'] = "disabled"
        self.butt6low['state'] = "disabled"
        self.butt6['state'] = "disabled"
        self.butt5['state'] = "disabled"
        self.butt41['state'] = "disabled"
        self.butt62['state'] = "disabled"
        self.butt61['state'] = "disabled"
        self.butt52['state'] = "disabled"
        self.butt456['state'] = "disabled"

    def getDice(self, ran):
        print(ran)
        if ran == 1:
            self.img = Image.open("image\dice1.jpg")
        elif ran == 2:
            self.img = Image.open("image\dice2.jpg")
        elif ran == 3:
            self.img = Image.open("image\dice3.jpg")
        elif ran == 4:
            self.img = Image.open("image\dice4.jpg")
        elif ran == 5:
            self.img = Image.open("image\dice5.jpg")
        elif ran == 6:
            self.img = Image.open("image\dice6.jpg")
        weight, height = self.img.size
        weight, height = int(weight*0.07), int(height*0.07)

        self.img = self.img.resize((weight, height))
        self.img = ImageTk.PhotoImage(self.img)

    def checkHiLo(self):
        result_dice = self.dice1 + self.dice2 + self.dice3
        if result_dice >= 12: #แต้มสูง 12-18
            self.result = "HIGH"
        elif result_dice == 11: #11 ไฮโล
            self.result = "11HILO"
        elif result_dice <= 10: #แต้มต่ำ 3-10
            self.result = "LOW"

    def placeDice(self):
        self.dice1 = self.ranNum()
        self.getDice(self.dice1)
        self.dice1img = tkinter.Label(image=self.img)
        self.dice1img.image = self.img
        self.dice1img.place(relx=0.87, rely=0.15, anchor='center')

        self.dice2 = self.ranNum()
        self.getDice(self.dice2)
        self.dice2img = tkinter.Label(image=self.img)
        self.dice2img.image = self.img
        self.dice2img.place(relx=0.92, rely=0.15, anchor='center')

        self.dice3 = self.ranNum()
        self.getDice(self.dice3)
        self.dice3img = tkinter.Label(image=self.img)
        self.dice3img.image = self.img
        self.dice3img.place(relx=0.89, rely=0.25, anchor='center')

    def shake(self):
        self.label2.place(relx=0.9, rely=0.15, anchor='center')
        root.update()
        time.sleep(1)
        self.label2.place(relx=0.9, rely=0.2, anchor='center')

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

        img = Image.open("image\money.png")
        weight, height = img.size
        weight, height = int(weight*0.23), int(height*0.23)

        img = img.resize((weight, height))
        img = ImageTk.PhotoImage(img)

        self.label4 = tkinter.Label(image=img)
        self.label4.image = img

        img = Image.open("image\people.png")
        weight, height = img.size
        weight, height = int(weight*0.18), int(height*0.18)

        img = img.resize((weight, height))
        img = ImageTk.PhotoImage(img)

        self.label5 = tkinter.Label(image=img)
        self.label5.image = img

    def placeObj(self):
        self.label1.place(relx=0.905, rely=0.89, anchor='center')
        self.label2.place(relx=0.9, rely=0.2, anchor='center')
        self.label4.place(relx=0.8325, rely=0.5, anchor='center')
        self.label5.place(relx=0.83, rely=0.4, anchor='center')
        self.name.place(relx=0.9, rely=0.4, anchor='center')
        self.money.place(relx=0.9, rely=0.5, anchor='center')
        self.monPay.place(relx=0.91, rely=0.6, anchor='center')

    def keepNum(self, id, moneyBet):
        if id == 1:
            self.mon1 = str(int(self.mon1.replace(" ", "0"))+moneyBet)
            self.butt1['text'] = "1\n\n%s" %(self.mon1)
        elif id == 2:
            self.mon2 = str(int(self.mon2.replace(" ", "0"))+moneyBet)
            self.butt2['text'] = "2\n\n%s" %(self.mon2)
        elif id == 3:
            self.mon3 = str(int(self.mon3.replace(" ", "0"))+moneyBet)
            self.butt3['text'] = "3\n\n%s" %(self.mon3)
        elif id == 4:
            self.mon4 = str(int(self.mon4.replace(" ", "0"))+moneyBet)
            self.butt4['text'] = "4\n\n%s" %(self.mon4)
        elif id == 5:
            self.mon5 = str(int(self.mon5.replace(" ", "0"))+moneyBet)
            self.butt5['text'] = "5\n\n%s" %(self.mon5)
        elif id == 6:
            self.mon6 = str(int(self.mon6.replace(" ", "0"))+moneyBet)
            self.butt6['text'] = "6\n\n%s" %(self.mon6)
        elif id == [1, 5]:
            self.mon15 = str(int(self.mon15.replace(" ", "0"))+moneyBet)
            self.butt15['text'] = "1 o 5\n\n%s" %(self.mon15)
        elif id == [1, 6]:
            self.mon16 = str(int(self.mon16.replace(" ", "0"))+moneyBet)
            self.butt16['text'] = "1 o 6\n\n%s" %(self.mon16)
        elif id == [2, 5]:
            self.mon25 = str(int(self.mon25.replace(" ", "0"))+moneyBet)
            self.butt25['text'] = "2 o 5\n\n%s" %(self.mon25)
        elif id == [1, 2, 3]:
            self.mon123 = str(int(self.mon123.replace(" ", "0"))+moneyBet)
            self.butt123['text'] = "1 o 2 o 3\n\n%s" %(self.mon123)
        elif id == [3, 6]:
            self.mon36 = str(int(self.mon36.replace(" ", "0"))+moneyBet)
            self.butt36['text'] = "3 o 6\n\n%s" %(self.mon36)
        elif id == [2, 4]:
            self.mon24 = str(int(self.mon24.replace(" ", "0"))+moneyBet)
            self.butt24['text'] = "2 o 4\n\n%s" %(self.mon24)
        elif id == [3, 5]:
            self.mon35 = str(int(self.mon35.replace(" ", "0"))+moneyBet)
            self.butt35['text'] = "3 o 5\n\n%s" %(self.mon35)
        elif id == [4, 1]:
            self.mon41 = str(int(self.mon41.replace(" ", "0"))+moneyBet)
            self.butt41['text'] = "4 o 1\n\n%s" %(self.mon41)
        elif id == [4, 5, 6]:
            self.mon456 = str(int(self.mon456.replace(" ", "0"))+moneyBet)
            self.butt456['text'] = "4 o 5 o 6\n\n%s" %(self.mon456)
        elif id == [5, 2]:
            self.mon52 = str(int(self.mon52.replace(" ", "0"))+moneyBet)
            self.butt52['text'] = "5 o 2\n\n%s" %(self.mon52)
        elif id == [6, 1]:
            self.mon61 = str(int(self.mon61.replace(" ", "0"))+moneyBet)
            self.butt61['text'] = "6 o 1\n\n%s" %(self.mon61)
        elif id == [6, 2]:
            self.mon62 = str(int(self.mon62.replace(" ", "0"))+moneyBet)
            self.butt62['text'] = "6 o 2\n\n%s" %(self.mon62)
        elif id == [5, "LOW"]:
            self.mon5Low = str(int(self.mon5Low.replace(" ", "0"))+moneyBet)
            self.butt5low['text'] = "5 LOW\n\n%s" %(self.mon5Low)
        elif id == [6, "LOW"]:
            self.mon6Low = str(int(self.mon6Low.replace(" ", "0"))+moneyBet)
            self.butt6low['text'] = "6 LOW\n\n%s" %(self.mon6Low)
        elif id == "11HILO":
            self.mon11Hiro = str(int(self.mon11Hiro.replace(" ", "0"))+moneyBet)
            self.butt11Hiro['text'] = "11 Hiro\n\n%s" %(self.mon11Hiro)
        elif id == "LOW":
            self.monLow = str(int(self.monLow.replace(" ", "0"))+moneyBet)
            self.buttLow['text'] = "LOW\n\n%s" %(self.monLow)
        elif id == "HIGH":
            self.monHigh = str(int(self.monHigh.replace(" ", "0"))+moneyBet)
            self.buttHigh['text'] = "HIGH\n\n%s" %(self.monHigh)
        self.checkList(id)

    def plusMoney(self):
        if self.result in self.bet: # ต่ำ สูง 11Hiro
            self.highLow()
        if self.dice1 in self.bet:
            self.onlyNum(self.dice1)
        if self.dice2 in self.bet:
            self.onlyNum(self.dice2)
        if self.dice3 in self.bet:
            self.onlyNum(self.dice3)
        if ([self.dice1, self.dice2]) in self.bet:
            self.twoNum(self.dice1, self.dice2)
        if ([self.dice1, self.dice3]) in self.bet:
            self.twoNum(self.dice1, self.dice3)
        if ([self.dice2, self.dice1]) in self.bet:
            self.twoNum(self.dice2, self.dice1)
        if ([self.dice2, self.dice3]) in self.bet:
            self.twoNum(self.dice2, self.dice3)
        if ([self.dice3, self.dice1]) in self.bet:
            self.twoNum(self.dice3, self.dice1)
        if ([self.dice3, self.dice2]) in self.bet:
            self.twoNum(self.dice3, self.dice2)
        if ([self.dice1, self.dice2, self.dice3]) in self.bet:
            self.triNum(self.dice1, self.dice2, self.dice3)
        if ([self.dice1, self.dice3, self.dice2]) in self.bet:
            self.triNum(self.dice1, self.dice3, self.dice2)
        if ([self.dice2, self.dice1, self.dice3]) in self.bet:
            self.triNum(self.dice2, self.dice1, self.dice3)
        if ([self.dice2, self.dice3, self.dice1]) in self.bet:
            self.triNum(self.dice2, self.dice3, self.dice1)
        if ([self.dice3, self.dice1, self.dice2]) in self.bet:
            self.triNum(self.dice3, self.dice1, self.dice2)
        if ([self.dice3, self.dice2, self.dice1]) in self.bet:
            self.triNum(self.dice3, self.dice2, self.dice1)
        if ([self.dice1, self.result]) in self.bet:
            self.low56(self.dice1)
        if ([self.dice2, self.result]) in self.bet:
            self.low56(self.dice2)
        if ([self.dice3, self.result]) in self.bet:
            self.low56(self.dice3)

    def highLow(self):
        if self.result == "HIGH":
            self.money['text'] = int(self.money['text'])+int(self.monHigh.replace(" ", "0"))*2
        elif self.result == "LOW":
            self.money['text'] = int(self.money['text'])+int(self.monLow.replace(" ", "0"))*2
        elif self.result == "11HILO":
            self.money['text'] = int(self.money['text'])+int(self.mon11Hiro.replace(" ", "0"))*7

    def onlyNum(self, dice):
        if dice == 1:
            self.money['text'] = int(self.money['text'])+int(self.mon1.replace(" ", "0"))*2
        elif dice == 2:
            self.money['text'] = int(self.money['text'])+int(self.mon2.replace(" ", "0"))*2
        elif dice == 3:
            self.money['text'] = int(self.money['text'])+int(self.mon3.replace(" ", "0"))*2
        elif dice == 4:
            self.money['text'] = int(self.money['text'])+int(self.mon4.replace(" ", "0"))*2
        elif dice == 5:
            self.money['text'] = int(self.money['text'])+int(self.mon5.replace(" ", "0"))*2
        elif dice == 6:
            self.money['text'] = int(self.money['text'])+int(self.mon6.replace(" ", "0"))*2

    def twoNum(self, dice1, dice2):
        if dice1 == 1 and dice2 == 5:
            self.money['text'] = int(self.money['text'])+int(self.mon15.replace(" ", "0"))*5
        elif dice1 == 1 and dice2 == 6:
            self.money['text'] = int(self.money['text'])+int(self.mon16.replace(" ", "0"))*5
        elif dice1 == 2 and dice2 == 5:
            self.money['text'] = int(self.money['text'])+int(self.mon25.replace(" ", "0"))*5
        elif dice1 == 3 and dice2 == 6:
            self.money['text'] = int(self.money['text'])+int(self.mon36.replace(" ", "0"))*5
        elif dice1 == 2 and dice2 == 4:
            self.money['text'] = int(self.money['text'])+int(self.mon24.replace(" ", "0"))*5
        elif dice1 == 3 and dice2 == 5:
            self.money['text'] = int(self.money['text'])+int(self.mon35.replace(" ", "0"))*5
        elif dice1 == 4 and dice2 == 1:
            self.money['text'] = int(self.money['text'])+int(self.mon41.replace(" ", "0"))*5
        elif dice1 == 5 and dice2 == 2:
            self.money['text'] = int(self.money['text'])+int(self.mon52.replace(" ", "0"))*5
        elif dice1 == 6 and dice2 == 1:
            self.money['text'] = int(self.money['text'])+int(self.mon61.replace(" ", "0"))*5
        elif dice1 == 6 and dice2 == 2:
            self.money['text'] = int(self.money['text'])+int(self.mon62.replace(" ", "0"))*5

    def triNum(self, dice1, dice2, dice3):
        if dice1 == 1 and dice2 == 2 and dice3 == 3:
            self.money['text'] = int(self.money['text'])+int(self.mon123.replace(" ", "0"))*10
        elif dice1 == 4 and dice2 == 5 and dice3 == 6:
            self.money['text'] = int(self.money['text'])+int(self.mon456.replace(" ", "0"))*10

    def low56(self):
        if dice == 5:
            self.money['text'] = int(self.money['text'])+int(self.mon5Low.replace(" ", "0"))*5
        elif dice == 6:
            self.money['text'] = int(self.money['text'])+int(self.mon6Low.replace(" ", "0"))*5

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
        self.open = Button(text="Show Dice", command=lambda: self.openDice(), font=("Arial", 18, ""), height=2, width=8, bd=5)

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
        self.open.place(relx=0.9, rely=0.70, anchor='center')

root = Tk()
root.title("Hiro")
root.resizable(False, False)
pageOne = PageOne()
root.mainloop()
