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