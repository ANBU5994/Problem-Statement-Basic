#You have three hidden numbers, and your mission is to find out which one is the 
#greatest. Write a program that can reveal the highest of these three numbers.
# 8A. Perform the above operation using ternary operator.

a=int(input("enter the number 1"))
b=int(input("enter the number 2"))
c=int(input("enter the number 3"))

if a>=b and a>c:
    print("a is bigger")
    
elif b>c and b>a:
    print("b is bigger") 
else:
    print("c is bigger")


