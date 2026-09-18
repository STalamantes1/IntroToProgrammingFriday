#What is a boolean? 
#A boolean is a value that is either TRUE or FALSE 
# print(5>10)
# print(10<20)
# print(3>=74)
# print("cat"=="Cat")

#Any expression that evaluates to True or False is a boolean expression 
#if statements use these to decided what to run 

#How can you create a conditional statement based on user input? 
# answer=int(input("Enter your percentage and I'll tell you what grade you have"))
# if answer >=90:
#     print("Congrats you have an A")
# elif answer=="no":
#     print("Exiting the program now")
# else:
#     print("Invalid Response")


#Comparison Operators 
# == equal to

# != not equal to

# < less than

# > greater than

# <= less than or equal to

# >= greater than or equal to

# score=85
# print(score>75)
# print(score<75)
# print(score==100)


#Using AND & OR 
# temp=72
# if temp>=72 and temp <=75:
#     print("This is comftable room temp")

#When using AND, both conditions must be TRUE 
#When using OR, at least one condition must be TRUE 

#I want this program to output ("You dont have class today")
# day="Saturday"
# is_holiday=False
# if day=="Saturday" or day=="Sunday" or is_holiday:
#     print("You dont have class today")
#this program compares multiple conditions at the same time

# day="Monday"
# is_holiday=False
# if day=="Saturday":
#     print("No class its saturday")
# elif day=="Sunday":
#     print("No class its sunday")
# elif is_holiday==False:  #False=True
#     print("Its a holiday")

#Chained Comparisons 
score=75
#how to write out 65 is <= score but less than 90
# if 60 <= score <90:  
#  #This is also the exact same as: score>=60 and score <90
#     print("Score is passing but not perfect")

#Using if + elif + else
#This is a simple 3 category example
#This program prints out the shipping cost based on the order price 
#When using any sort of money input we will use float
# total=float(input("Enter your order total: "))
# if total<25:
#     print("Shipping is $10")
# #if user input is less then 50, they get $5 shipping
# elif total<50:
#     print("You get $5 shipping! ")
# else:
#     print("Free shipping")

# #Compare == & is 
# list1=[1,2,3]
# list2=[1,2,3]
# list3=list1
# print(list1==list2) #True: Contents are equal 
# print(list1 is list2) #False: Different objects in memory 
# print(list1==list3) #True: content still the same
# print(list1 is list3) #True: lsit3 points to the same object as list1

#== compares values/content
#is compares identity(Are they literally the same object? )

#Two different boxes can have the same stuff inside (==)
#But they're still two different boxes(is)

#multi brand example
#program that tells me if the number is postitive or negative 
# number=int(input("Enter your number"))
# if number<0:
#     print("Negative")
# elif number>0:
#     print("positive")
# else:
#     print("Your number is 0")


# total=float(input("Enter money"))
# if total>20:
#     print("10%")
# elif total>150:
#     print("5%")
# else:
#     print("No discount")


password=input("Enter your password: ")
 #len is used to count how many characters an obj is
if len(password)>=8:
    print("Password is the right length")
else:
    print("Password is too short")
