'''range(stop) #by default start as 0
range(start,stop) #ranging start till stop
range(start, stop, step) #step = numnber of jumps

stop=0
range (stop)

for x in range (0,10,2):
    print (x)   
    
for x in range (10,0,-1):
    print (x)

for i in range (1,6):
    print("*" * i)
    
for i in range (0,9,1):
    print("*" *i)
    print("++++++++")
    for i in range (7,0,-1):
        print("*" *i)


for pyramid:
x=5
for i in range(1,x+1):
    print(" " *(x - i) + "*" *(2*i -1)  )

for square:
x=6
for i in range(1,11):
    print(" + " *10)

for inverted pyramid:

x=5
for i in range(x,0,-1):
    print(" " *(x - i) + "*" *(2*i -1)  )
    
    
code a program, that ask you for a pattern out 4,
also, ask repeatedly for another pattern or break!


while True:
    print("Draw 4 Pattern For Unlocking")
    user=int(input("1 for triangle: \n2 for rectangle: \n3 for square: \n4 for circle:")) 
    
    if user==1:        
        x=4
        for i in range(x,0,-1):
            print(" " *(x - i) + "*" *(2*i -1) )
            
    elif user==2:
        x=6
        for i in range(x,0,-1):
            print(" " *(x - i) + "*" *(2*i -1) )
     
    elif user==3:
        x=8
        for i in range(x,0,-1):
            print(" " *(x - i) + "*" *(2*i -1) )
    
    elif user==4:
        x=10
        for i in range(x,0,-1):
            print(" " *(x - i) + "*" *(2*i -1) )
    rep=int(input("Press 1 for continue or 0 to break!"))
    if rep==1:
        continue
    
    else:
        print("Thanks")
        break
    
else:
    print("invalid Pattern")'''


#hollow square:

rows=5
for x in range(rows):
    if x == 0 or x == (rows-1):
        print("*" *rows)
    else:
        print("*" +  " " *(rows-2) + "*")
