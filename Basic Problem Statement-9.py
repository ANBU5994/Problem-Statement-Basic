'''You have a year in mind, and your task is to write a program that determines if this year 
is a leap year. Can you figure out if it has an extra day in February?
'''






def is_leap(year):
   
    if year % 4 == 0: 
        if  year % 100 == 0: # Check May Be a Century
            if year % 400 == 0: # 
                return("The year is leap year it has more Days In Feburary") 
            else :
                return("The year is Not leap year")
        else:
             return("The year is leap year it has more Days In Feburary")
    else :
        return("The year is Not leap year")
    
    
n=int(input("enter the year to check the year is leap year or not : "))
print(is_leap(n))