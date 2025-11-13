'''In python there are four forms of if … else statement:

1.	if statement.
2.	if…else statement.
3.	if…elif…else statement.
4.	Nested if statement.


#1.	if statement:

age=int(input("Enter Your age"))
if age>18:
    print("You can apply for license")
print("Speed thrills but kills")


#2.	if...else statement:

age=int(input("Enter Your age"))
if age>18:
    print("You can apply for license")
else:
    print("Be calm & patienate")


#3.	if….elif….else statement:
handsome='true'
good_salary='true'
if handsome=='true' and good_salary=='true':
    print("you will mary with a super model")
    
elif handsome!='true' and good_salary=='true':
    print("you will mary with a city girl")

elif handsome=='true' and good_salary!='true':
    print("you will mary with your relative's girl")

else:
    print("you are not eligible for super model")


#Nested if statement:

age=17
own_car="false"

if (age>=18):  			 #(outer if statement)
    
    if (own_car=="true"): #(inner if statement)
        print("Drive your car")
   
    else:	 			#(inner else statement)
        print("Work hard & purchase a new car")
        
else:					#(outer else statement)
    print("your not eligible")'''