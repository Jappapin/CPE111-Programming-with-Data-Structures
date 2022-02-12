#1
def Cal_Resis(List_R):
    try:
        result = 0
        for i in List_R:
            result = (1/i) + result
        print(1/result)
    except:
        print("The parameter should be LIST type\nExample : [2,2]")
#test case
Cal_Resis([2,2])
Cal_Resis(2)
Cal_Resis("eiei")

#2
money = input('Enter the amount of money (no-.25,-.50,-.75): ')
Money = int(money)
Ten = Money//10
Five = ( Money - (Ten*10) )//5
One = Money - ((Ten*10)+(Five*5))
print("You received %.0f 10฿ coin(s),%.0f 5฿ coin(s)and %.0f 1฿ coins"%(Ten,Five,One))

#3
def check90triangle(a,b,c):
    try:
        if (a*a) == (b*b) + (c*c) or (b*b) == (a*a) + (c*c) or (c*c) == (b*b) + (a*a):
            print('This is the right triangle.')
        else:
            print('This is NOT the right triangle.')
    except:
        print('Something went wrong with your parameter, make sure they are numbers.')
#testcase
check90triangle(3,4,5)
check90triangle(4,5,3)
check90triangle("Hi","H","i")

#4
started = input("started station :")
destination = input("destination station :")
try:
    stations = ["A","B","C","D","E","F","G"]
    st_ = stations.index(started)
    des_ = stations.index(destination)
    distance = abs(st_ - des_)
    prices = [0,25,37,37,45,45,60]
    pr = prices[dis]
    print("Prices for %.0f station(s) is %.0f Baht."%(distance,pr))
except:
    print("Enter the EXISTED station (A,B,C,D,E,F,G)")

#5
import math
cost = float(input("Enter the cost of diner ( 0 to stop): "))
while cost != 0:
    people = int(input("Enter the number of people : "))
    pay = math.ceil(cost/people)
    tip = (pay*people) - cost
    print("Each person must pay : %.2f Baht"%pay)
    print("and tip for the waiter is :%.2f Baht"%tip)
    cost = float(input("Enter the cost of diner : "))