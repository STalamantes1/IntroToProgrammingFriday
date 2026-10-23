#Week 10 Notes, Functions 
#What is a function? 
# A function is a named set of instructions you can run whenever you want 
#Functions let us write code once and reuse it when we need it 

#Def(define) a function: create a function by starting with def 
#Call a function: run the function by using its name with parantheses()
#Parameter: Placeholder variable inside the function definition 
#Argument: THe real value that we pass into the function via the parameter 

#Create a function that says "Hello"
# def say_hello():
#     print("Hello")
# #Call the function 
# say_hello()

#def tells Pythons: "Im defining a function"
#Coder inside the function must be indented 
#Nothing runs until you call it 

#Parameters and Arguments 
# def greet(name):
#     #name is a parameter(a placeholder)
#     print(f"Hello, {name}")
# name=input("Enter your name: ")
# greet(name)
# greet("Carl")
#Paramaters are like blanks. Arguments fill them in 

#The only time we need parameters is when we are passing information from outside the function, into the function
# def greet():
#     name=input("Enter your name")
#     print(f"Hello, {name}")
# greet()

#Print vs Return 
# A function that prints: 
# def hello_print():
#     print("hello world")
# # #This shows the text to the user 
# # #But it does not give a value back to the rest of the program 

# # #A function that Returns :
# # def hello_return():
# #     name=input("Enter your name: ")
# #     return f"Hello, {name}"
# # #This sends a value back to wherever the function was called 
# # # The caller can store it, print it, etc 

# # msg=hello_return()
# # print(msg)

# result=hello_print()
# print(result) #This will print none, because hello_print doesn't return a value back to the function 

#Print is for the user. Return is for the progam 

#Function example 
#Calc program

def calc(num1,num2):
    operator=input("What sort of math do you want to do: +,-,*,/")
    #Use if/else to decide what to do 
    #perform the math 
    #Print or Return the result 
    if operator=="+":
        return num1+num2

# print(calc(1,3))#function now has the value of 4 


#Fake Loop 
#A function can call itself, this is called recursion 
#A function can behave like a loop if it repeats until a condtion is met 
#if a function is calling itself, it must have a stop condition

#A function that prompts user if they want to continue
# If user says yes, ask them again
# , if user doesnt want to continue "Loop" stops
# def play_again():
#     answer=input("Again? (y/n): ").lower()
#     if answer=="y":
#         play_again()#Calls itself again 
#     else:
#         print("goodbye")
# play_again()

def length(color):
    return len(color)

color=input("What your fav color: ")
print(length(color))