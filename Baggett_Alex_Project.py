itemprice = float(input("How much the items that was given cost: "))
salestax = 1.07

(dx) = itemprice*salestax
print(dx) 
#amount of money that needs to be payed off

money = float(input("What was the amount given to the register: "))
dx = dx - money

if dx < 0:
    vc = dx * -1
    change = str(vc)
    print("amount of money that needs to be given back: " + change)
    




