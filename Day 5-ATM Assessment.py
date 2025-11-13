''' ATM Assessment:

code a program, that can work like a flow of ATM Machine!

1:pin-code
2:type (current, default, savings)
3:fast cash, cash-withdrawal, balance inquiry, transfer, bill-payment
4:cash receipt (yes/no)
5:cash receive'''

time=0
while time<=3:
    pin=input("Enter a Pin Code:")
    print(f"Limits you have for right pin code {time}:")
    
    while pin=="1234":
        print("Welcome to ATM")
        cat=int(input("which type of banking you want to continue, \n1: current : \n2: savings : \n3: default:"))
        if cat==1:
            inp=int(input("select your Prefered Transaction, \n1: Fast Cash : \n2: cash-withdrawal : \n3: balance inquiry : \n4: transfer :\n5: bill-payment:"))
            if inp==1:
                print("Welcome to fast cash!")
                amu=int(input("select an amount , \n1: 5000 : \n2: 10000 : n\3: 15000 : n\4: 20000:"))
                if amu==1 or amu==2 or amu==3 or amu==4:
                    print("Transaction succefully done! thank you for using our ATM services")
                    rp=input("cash receipt (y/n):").lower()
                    if rp=="y":
                        print("Receipt generated")
                    else:
                        print("Wrong input")
                        
    else:
        print("You have entered a wrong pin, please try again")
        time -=1
        continue

else:
    print("Account Locked!")