'''You have a number to examine, and your mission is to write a program that checks 
whether this number can be divided evenly by 27. Can you find out if it‟s a multiple of 
27?'''
def num(n):
    if (n %27==0):
        for i in range(1,11,1):
            print("27 x",i,"=",i*27)
            
    else :
        return("the number is not divided by 27")
    
n=int(input("To check the numbr if it is divided by 27 and the multiples of 27"))
print(num(n))    
