'''You have a number in hand, and your challenge is to write a program that 
determines whether this number can be evenly divided by 100. Can you uncover if it‟s a 
multiple of 100 or not?

'''

def num(n):
    if (n %100==0):
        return("the number ",n ,"is divided by 100")
    else :
        return("the number" ,n," is not divided by 100")
n=int(input("To check the numbr if it is divided by 100 or not "))
print(num(n))    