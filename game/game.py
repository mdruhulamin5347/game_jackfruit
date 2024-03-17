import random
from time import sleep
import webbrowser as auto
n =int(input("HOW MANY MAN YOU ARE ALL  : "))
m =int(input("HOW MANY MAN CAN YOU TAKE :"))
list1 = []
bonnus_list =['0','0','0','5','0','0','0','10','0','0','0']
for i in range(n):
    name1 =input("Enter your name :")
    list1.append(name1)
if list1:
    for i in range(m):
        randomnumber =random.randint(0,n-1)
        bonnus_money =random.randint(0,10)
        print("Congratulation! " + list1[randomnumber] + " tomorrow is your market "+ "And Your bonnus is " + bonnus_list[bonnus_money] +" taka !!!!")
sleep(10)
auto.open("sites.google.com/view/nahidul407/home")




