
while True:
        paymentoption = input("What is the payment option (Cash/Card):")
        if paymentoption == "Cash":
            break
        else:
            if paymentoption == "Card":
                break
#vaildates the paymention options
#paymentoption is the variable where you enter cash or card

while True:
        itemprice = float(input("How much the items that was given cost: "))
        if itemprice > 0:
            break
        else:
            print("The number is is the negatives. Please input again.")
#vaildates the items cost
#itemprice is the amount the items that was given cost

salestax = 1.07
(aftersalestax) = itemprice*salestax
print(aftersalestax)
#amount of money that needs to be payed off with salestax
#salestax is used to get the variable aftersalestax
#aftersalestax is the price of the items with salestax


while True:
    money = float(input("What was the amount given to the register: "))
    finalpay = aftersalestax - money
    if finalpay < 0:
        break
    else:
        print("The number is is the negatives or was less then the price. Please input again.")
#vaildates the amount give to the register
#money is used for the amount that is given to the employee
#finalpay is the negative number of the amount that needs to be given back to the customer
#does the math for the amount given to employee

if finalpay < 0:
    vc = finalpay * -1
    change = str(vc)
    print("Amount of money that needs to be given back: " + change)
#tell the amount of money that the employee needs to give back
#vc is to change the negative number into a postive number for easier reading
#change is the amount of money that needs to be given to the customer


if paymentoption == 'Cash':
    print("The customer used cash to pay for items.")
else:
    if paymentoption == 'Card':
        print("the customer used card to pay for items.")
#tell what payment they used
