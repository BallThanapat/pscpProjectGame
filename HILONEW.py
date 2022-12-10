import random
'''dice123'''
money = int(input("ลงเท่าไหร่"))
yyy = input("เลือกแทงแบบไหน")
def dice():
    '''dice'''
    dice1 = [1, 2, 3, 4, 5, 6]
    dice2 = [1, 2, 3, 4, 5, 6]
    dice3 = [1, 2, 3, 4, 5, 6]
    result_num = (random.choice(dice1))+(random.choice(dice2))+(random.choice(dice3))
    return result_num
'''condition'''
def condition1():
    '''condition'''
    print("H:สูง")
    print("L:ต่ำ")
    print("M:กล่าง")
    xxx = (input("แทงอะไร:"))
    dice1 = [1, 2, 3, 4, 5, 6]
    dice2 = [1, 2, 3, 4, 5, 6]
    dice3 = [1, 2, 3, 4, 5, 6]
    dice1ran = random.choice(dice1)
    dice2ran = random.choice(dice2)
    dice3ran = random.choice(dice3)
    print(dice1ran)
    print(dice2ran)
    print(dice3ran) 
    dice_result1 = dice1ran + dice2ran + dice3ran
    print("ผลรวมคือ:" , dice_result1)
    if dice_result1 >= 12:   #แต้มสูง 12-18
        xyz = "H"
    elif dice_result1 == 11: #11 ไฮโล
        xyz = "M"
    else:                   #แต้มต่ำ 3-10
        xyz = "L"
    if xyz == xxx:
        print("You win ",money*2)
    else:
        print("You Lost ",money*0)
'''teng'''
def condition2():
    '''teng'''
    number = int(input("แทงเลขไร"))
    dice1 = [1, 2, 3, 4, 5, 6]
    dice2 = [1, 2, 3, 4, 5, 6]
    dice3 = [1, 2, 3, 4, 5, 6]
    dice1ran = random.choice(dice1)
    dice2ran = random.choice(dice2)
    dice3ran = random.choice(dice3)
    print(dice1ran)
    print(dice2ran)
    print(dice3ran)  
    if number == dice1ran or number == dice2ran or number == dice3ran:
        print("win")
        print("Balance", money*2)
    else:
        print("You lose")
        print("Balance")
def condition3():
    '''tood'''
    number = int(input())
    dice1 = [1, 2, 3, 4, 5, 6]
    dice2 = [1, 2, 3, 4, 5, 6]
    dice3 = [1, 2, 3, 4, 5, 6]
    dice1ran = random.choice(dice1)
    dice2ran = random.choice(dice2)
    dice3ran = random.choice(dice3)
    print(dice1ran)
    print(dice2ran)
    print(dice3ran)  
    if dice1ran == number and dice2ran == number:
        print("You win")
        print("Balance", money*5)
    elif dice1ran == number and dice3ran == number:
        print("You win")
        print("Balance", money*5)
    elif dice2ran == number and dice3ran == number:
        print("You win")
        print("Balance", money*5)
    else:
        print("you lost")
        print("Balance = 0")
    
if yyy == "1":
    condition1()
elif yyy == "2":
    condition2()
elif yyy == "3":
    condition3()
    