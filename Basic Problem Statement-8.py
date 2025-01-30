'''You have two numbers, and your challenge is to write a program that performs both 
addition and subtraction with them. However, if any subtraction results in a negative 
number, display it as a positive value. How will you tackle this and show the final 
results? '''

def sum(a,b):
    print(abs(a+b))
    c=abs(a-b)
    print(c)

a=int(input("enter the number a"))
b=int(input("enter the number b"))

sum(a,b)