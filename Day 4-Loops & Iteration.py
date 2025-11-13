#Loops/iteration in Python!

#1:while
#2:for

#while loop requires condition! (iterates /repeats) the block till the
#condition is true!

'''
num=1
while num==1:#True
    print("this is loop" ,num) #(Loop continues unbreakable)
    
num=1
while num<=10:#True
    print("this is loop" ,num)
    #num = num+1 #increment
    num +=1
    
num=10
while num>=1:#True
    print("this is loop" ,num)
    #num = num-1 #decrement
    num -= 1


#code a program, which takes input from user for a table!

num=int(input("Enter a number, for a table"))

i=1
while i<=10:
    #print(f"{num} x {i} = {num*i}") #formatted string #2 x 1 =2
    print(num, "x",i,"=",num*i)
    i +=1 #i = i+1
    
while true:
    num=int(input("Enter a number, for a table"))

i=1
while i<=10:
    print(f"{num} x {i} = {num*i}") #formatted string #2 x 1 =2
    i +=1 #i = i+1
    continue
    #break

while true:
    num=int(input("Enter a number, for a table"))

num2=3
i=1
while i<=10:
    print(f"{num2} x {i} = {num2*i}") #formatted string #2 x 1 =2
    i +=1 #i = i+1
    if num2 == "x":
        continue
    else:
        break

while true:
    num=int(input("Enter a number, for a table"))
    i=1
    while i<=10:
        print(f"{num} x {i} = {num*i}") #formatted string #2 x 1 =2
        i +=1 #i = i+1
        user=input("Do you want to continue?: (y/n)").lower()
        if user=="y":
            continue
        else:
            print ("Task Completed")
            break

#Code a program, for guess the number

secret = 8
guess=0

while guess!=secret:
    guess=eval(input("Enter a number to guess"))
    if guess>secret:
        print("Too High")
    elif guess<secret:
        print("Too Low")
    else:
        print("Congrats!")
        

inp=3

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

            print("Congrats!")'''


inp=3

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
            print("Congrats!")
else:
    print("You Lost!")
    
    
inp = 3
while inp> 0:
    secret = 8
    guess = eval(input(f"{inp} times left | Enter a number to guess: "))

    if guess == secret:
        print("congrats You guessed it right!")
        break
    else:
        print("lost")
        inp -= 1
else:
    print("Game over! You are out of attempts.")
   
   
inp = 6
while inp > 2:
    secret = 20
    guess = eval(input(f"{inp} times left | Enter a number to guess: "))

    if guess != secret:
        print("you guessed it wrong!")
        break
    else:
        print("try again")
        inp -= 2
else:
    print("System does not require more attempts")
