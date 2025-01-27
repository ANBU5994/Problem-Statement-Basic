#You have two secret numbers, and you need to figure out how they relate to each other 
#using a set of special tools. Your challenge is to write a program that uses these tools—>, 
#>=, <, <=, ==, and !=—to uncover all the secrets about how these numbers compare. 



def num(a,b):
    if a==b:
        print(a ,"and", b ,"are equal")
    elif a>=b:
        print(a,"is Bigger")
    elif a>=b:
        print(a,"is Bigger")
    elif a<=b:
        print(b,"is Bigger")
    elif a<=b:
        print(a,"is Bigger")
    
    elif a!=b:
        print("a is not equal to b")

a = int(input("enter the first secret number"))
b = int(input("enter the second secret number"))        
try:
    res=num(a,b)
    print(res)
except:
    print("enter the correct value")