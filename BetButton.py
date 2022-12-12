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
btn7 = Button(root,text="O",command=lambda: keepnum([1,5])).pack()
btn8 = Button(root,text="O",command=lambda: keepnum([1,6])).pack()
btn9 = Button(root,text="O",command=lambda: keepnum([2,5])).pack()
btn10 = Button(root,text="O",command=lambda: keepnum([1,2,3])).pack()
btn11 = Button(root,text="O",command=lambda: keepnum([3,6])).pack()
btn12 = Button(root,text="O",command=lambda: keepnum([2,4])).pack()
btn13 = Button(root,text="O",command=lambda: keepnum([3,5])).pack()
btn14 = Button(root,text="O",command=lambda: keepnum([4,1])).pack()
btn15 = Button(root,text="O",command=lambda: keepnum([4,5,6])).pack()
btn16 = Button(root,text="O",command=lambda: keepnum([5,2])).pack()
btn17 = Button(root,text="O",command=lambda: keepnum([6,1])).pack()
btn18 = Button(root,text="O",command=lambda: keepnum([6,2])).pack()
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
    elif id==[1,5]:
        lst.append(id)
    elif id==[1,6]:
        lst.append(id)
    elif id==[2,5]:
        lst.append(id)
    elif id==[1,2,3]:
        lst.append(id)
    elif id==[3,6]:
        lst.append(id)
    elif id==[2,4]:
        lst.append(id)
    elif id==[3,5]:
        lst.append(id)
    elif id==[4,1]:
        lst.append(id)
    elif id==[4,5,6]:
        lst.append(id)
    elif id==[5,2]:
        lst.append(id)
    elif id==[6,1]:
        lst.append(id)
    elif id==[6,2]:
        lst.append(id)
    elif id==[5,"LOW"]:
        lst.append(id)
    elif id==[6,"LOW"]:
        lst.append(id)
    elif id=="11HILO":
        lst.append(id)
    elif id=="LOW":
        lst.append(id)
    elif id=="HIGH":
        lst.append(id)
    print (lst)

#เงื่อนไขคำนวณเงิน
def condition2():
    result,dice1,dice2,dice3 = condition()
    if result in lst:
        print("yes0")
    if dice1 in lst:
        print("yes1")
    if dice2 in lst:
        print("yse2")
    if dice3 in lst:
        print("yes3")
    if ([dice1,dice2]) in lst:
        print("tood1")
    if ([dice1,dice3]) in lst:
        print("tood2")
    if ([dice2,dice1]) in lst:
        print("tood3")
    if ([dice2,dice3]) in lst:
        print("tood4")
    if ([dice3,dice1]) in lst:
        print("tood5")
    if ([dice3,dice2]) in lst:
        print("tood6")
    if ([dice1,dice2,dice3]) in lst:
        print("tood7")
    if ([dice1,dice3,dice2]) in lst:
        print("tood8")
    if ([dice2,dice1,dice3]) in lst:
        print("tood9")
    if ([dice2,dice3,dice1]) in lst:
        print("tood10")
    if ([dice3,dice1,dice2]) in lst:
        print("tood11")
    if ([dice3,dice2,dice1]) in lst:
        print("tood12")
    if ([dice1,result]) in lst:
        print("tood13")
    if ([dice2,result]) in lst:
        print("tood13")
    if ([dice3,result]) in lst:
        print("tood13")

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

#เคลียร์ list เพื่อเริ่มใหม่
def restart():
    lst.clear()

#กดเพื่อเริ่มเช็คเงื่อนไข
btn_start = Button(root,text="START",command=lambda: condition2()).pack()
btn_reset = Button(root,text="RESTART",command=lambda: restart()).pack()

root.geometry("500x800")
root.mainloop()
