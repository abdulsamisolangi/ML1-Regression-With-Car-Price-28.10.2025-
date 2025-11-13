#Decision In Python

#Logical Operators

#and # if <condition =eg: password == "Rafay">

#, or, not

'''per=int(input("Enter a value"))

if per >80 and per <90:
    print ("True" , per)
else:
    print ("Condition is not true")

per=int(input("Enter a value"))

if per >80 or per<90 and per>85:
    print ("True" , per)
else:
    print ("Condition is not true")'''
    
    
#code a python for mobile phone shop,
#which recommmends you a mobile phone as per your given feature!
    
#budget, memory, camera, brand

'''Budget=eval(input("Enetr your budget"))
Camera=int(input("press 1: for 30 mp, \n press 2: 60 mp, \n press 3: 90 mp"))
Memory=int(input("press 1: for 4/128gb, \n press 2: 6\256gb, \n press 3: 8\512gb"))
Brand=int(input("press 1: for Tecno, \n press 2: Infinix, \n press 3: Oppo"))

if budget >50000 and memory==1 and camera==1 and brand==1:
    print ("Most Recommended for you: Tecno Camon 20, Tecno Camon 30, Tecno Camon 40")
    
elif budget >60000 and memory==2 and camera==2 and brand==2:
    print ("Most Recommended for you: Infinix 30, Infinix 40, Infinix 50")
    
elif budget >70000 and memory==3 and camera==3 and brand==3:
    print ("Most Recommended for you: Oppo A3, Oppo A4, Oppo A5")

else:
    print ("Budget is too low")

    
#nested if in decisions

age=eval(input("enter your age:"))

if age>=18:
    print("Welcome to University Website")
    std=int(input("Press 1: for Engineering Univ, \n press 2: for Medical Univ, \n press 3: for Law Univ, \n press 4: Technical Univ"))
    if std==1:
        per=int(input("Welcome To Engineering University, /n Enter Your Percentage:"))
        if per >=50:
            print ("Eligible")
        else:
            print("Not Eligible")
else:
    print ("you are under age, age limit is minimum 18!")

    if age>=18:
        print("Welcome to University Website")
        std=int(input("Press 1: for Engineering Univ, \n press 2: for Medical Univ, \n press 3: for Law Univ"))
        if std==1:
            per=int(input("Welcome To Engineering Univ, \n Enter Your Percentage:"))
            if per >=50:
            print ("Eligible")
        else:
            print("Not Eligible")
    elif std==2:
        per=int(input("Welcome To Medical Univ, \n Enter Your Percentage:"))
        if per >=60:
            print ("Eligible")
        else:
            print("Not Eligible")
    elif std==3:
        per=int(input("Welcome To Law Univ, \n Enter Your Percentage:"))
        if per >=55:
            print ("Eligible")
        else:
            print("Not Eligible")        
else:
    print ("you are under age, age limit is minimum 18!")


age=int(input("Enter Your Age"))
per=int(input("Enter Your Percentage"))   
    
if age>=25:
    print("Welcome to Cricket Category in University")
    std=int(input("Press 1: for 1st class category, \n press 2: 2nd class category, \n press 3: for 3rd category"))
    if std==1:
        fitness_level=int(input("Welcome To 1st class category, /n Enter Your Level"))
        if per >=60inp=3

while inp>=1:
    secret=8
    guess=0
    while guess!=secret:
        guess=eval(input(f"{inp} times left | Enter a number to guess"))
        if guess>secret:
            print("Too High!")
        elif guess<secret:
            print("Too Low")
            inp -=1
            break
        else:

            print("Congrats!")''':
            print ("Eligible")
        else:
            print("Not Eligible")
    elif std==2:
        fitness_level=int(input ("Welcome To 2nd class category, /n Enter Your Level"))
        if per >=50:
            print ("Eligible")
        else:
            print("Not Eligible")
    elif std==3:
        fitness_level=int(input("Welcom To 3rd class category, /n Enter Your Level"))
        if per >=45:
            print ("Eligible")
        else:
            print("Not Eligible")        
else:
    print("you are Not Fit, minimum level is 45!")'''