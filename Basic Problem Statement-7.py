'''Write a program to check the given number is divisible by both three and four if it is so print good morning.
 If the number is divisible by only four, but not by three then print good afternoon
 if it is divisible by only three and not by four, then good evening, otherwise, good night.'''
def num (n):
    if n%3==0 and n%4==0:
        print("Good MoRNING")
    elif n%4==0:
        print("Good afternoon")
    elif(n%3==0):
        print("good evening")
    else:
        print("Good Night")
n =int(input("enter the number "))        
num(n)