import tkinter
from tkinter import *
import random
root = Tk()
root.title("Hilo")

# แรนดอมเลข
def ranNum():
    return random.randint(1, 6)

#ปุ่มbutton
btn1 = Button(root,text="O",command=lambda: keepnum(1)).pack()
btn2 = Button(root,text="O",command=lambda: keepnum(2)).pack()
btn3 = Button(root,text="O",command=lambda: keepnum(3)).pack()
btn4 = Button(root,text="O",command=lambda: keepnum(4)).pack()
btn5 = Button(root,text="O",command=lambda: keepnum(5)).pack()
btn6 = Button(root,text="O",command=lambda: keepnum(6)).pack()
btn7 = Button(root,text="O",command=lambda: keepnum("15")).pack()
btn8 = Button(root,text="O",command=lambda: keepnum("16")).pack()
btn9 = Button(root,text="O",command=lambda: keepnum("25")).pack()
btn10 = Button(root,text="O",command=lambda: keepnum("123")).pack()
btn11 = Button(root,text="O",command=lambda: keepnum("36")).pack()
btn12 = Button(root,text="O",command=lambda: keepnum("24")).pack()
btn13 = Button(root,text="O",command=lambda: keepnum("35")).pack()
btn14 = Button(root,text="O",command=lambda: keepnum("41")).pack()
btn15 = Button(root,text="O",command=lambda: keepnum("456")).pack()
btn16 = Button(root,text="O",command=lambda: keepnum("52")).pack()
btn17 = Button(root,text="O",command=lambda: keepnum("61")).pack()
btn18 = Button(root,text="O",command=lambda: keepnum("62")).pack()
btn19 = Button(root,text="O",command=lambda: keepnum("5LOW")).pack()
btn21 = Button(root,text="O",command=lambda: keepnum("6LOW")).pack()
btn20 = Button(root,text="O",command=lambda: keepnum("11HILO")).pack()
btn22 = Button(root,text="O",command=lambda: keepnum("LOW")).pack()
btn23 = Button(root,text="O",command=lambda: keepnum("HIGH")).pack()

lst = []

#เงื่อนไขbutton
def keepnum(id):
    if id==1:
        lst.append(id)
    elif id==2:
        lst.append(id)
    elif id==3:
        lst.append(id)
    elif id==4:
        lst.append(id)
    elif id==5:
        lst.append(id)
    elif id==6:
        lst.append(id)
    elif id=="15":
        lst.append(id)
    elif id=="16":
        lst.append(id)
    elif id=="25":
        lst.append(id)
    elif id=="123":
        lst.append(id)
    elif id=="36":
        lst.append(id)
    elif id=="24":
        lst.append(id)
    elif id=="35":
        lst.append(id)
    elif id=="41":
        lst.append(id)
    elif id=="456":
        lst.append(id)
    elif id=="52":
        lst.append(id)
    elif id=="61":
        lst.append(id)
    elif id=="62":
        lst.append(id)
    elif id=="5LOW":
        lst.append(id)
    elif id=="6LOW":
        lst.append(id)
    elif id=="11HILO":
        lst.append(id)
    elif id=="LOW":
        lst.append(id)
    elif id=="HIGH":
        lst.append(id)
    print (lst)

def condition2():
    result,dice1,dice2,dice3 = condition()
    if result in lst and dice1 in lst and dice2 in lst and dice3 in lst:
        print("lucky")
    elif result in lst and dice1 in lst and dice2 in lst:
        print("lucky2")
    elif result in lst and dice1 in lst:
        print("lucky3")
    elif result in lst and dice2 in lst:
        print("lucky4")
    elif result in lst and dice3 in lst:
        print("lucky5")
    elif dice1 in lst and dice2 in lst:
        print("lucky6")
    elif dice1 in lst and dice3 in lst:
        print("lucky7")
    elif dice2 in lst and dice3 in lst:
        print("lucky7")
    elif result in lst:
        print("yes0")
    elif dice1 in lst:
        print("yes1")
    elif dice2 in lst:
        print("yse2")
    elif dice3 in lst:
        print("yes3")

def condition():
    dice1 = ranNum()
    dice2 = ranNum()
    dice3 = ranNum()
    result_dice = dice1+dice2+dice3
    if result_dice >= 12:   #แต้มสูง 12-18
        result = "HIGH"
        print("HIGH")
    elif result_dice == 11: #11 ไฮโล
        result = "11 HILO"
        print("11 HILO")
    elif result_dice <= 10: #แต้มต่ำ 3-10
        result = "LOW"
        print("LOW")
    print(dice1, dice2, dice3)
    return result,dice1,dice2,dice3

#กดเพื่อเริ่มเช็คเงื่อนไข
btn_start = Button(root,text="START",command=lambda: condition2()).pack()

root.geometry("500x800")
root.mainloop()