import tkinter
from tkinter import *
import random
root = Tk()
root.title("Hilo")
#แรนดอมเลข
# def ranNum():
#     return random.randint(1, 6)
# dice1 = ranNum()
# dice2 = ranNum()
# dice3 = ranNum()
# print(dice1, dice2, dice3)

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
btn19 = Button(root,text="O",command=lambda: keepnum(["5LOW"])).pack()
btn20 = Button(root,text="O",command=lambda: keepnum(["11HILO"])).pack()
btn21 = Button(root,text="O",command=lambda: keepnum(["6LOW"])).pack()
btn22 = Button(root,text="O",command=lambda: keepnum(["LOW"])).pack()
btn23 = Button(root,text="O",command=lambda: keepnum(["HIGH"])).pack()

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
    elif id==["5LOW"]:
        lst.append(id)
    elif id==["11HILO"]:
        lst.append(id)
    elif id==["6LOW"]:
        lst.append(id)
    elif id==["LOW"]:
        lst.append(id)
    elif id==["HIGH"]:
        lst.append(id)

root.geometry("500x500")
root.mainloop()