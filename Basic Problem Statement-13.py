'''You‟re tasked with creating a simple calculator using a while loop and a switch 
statement. Your program should repeatedly prompt the user to choose an arithmetic 
operation (like addition, subtraction, multiplication, or division) and then perform the 
selected operation based on user input. How will you set up your while loop and 
switch case to keep the calculator running until the user decides to exit '''

while True : #to enter the menu driven program 
    x=int(input("choose the operation \n For add Press 1 \n  For sub Press 2 \n For Mul press 3 \n For Div press 4 ,\n Press 5 For Exit" ))   
    
    if x==5:
        print("exit the program ")
        break
    
    a=int(input("enter the A :"))
    b=int(input("Enter the B :"))
            
    if x==1:
        print(a+b) 
    elif x==2:
        print(a-b)
    elif x==3:
        print(a*b)
    elif x==4:
        print(a/b)
    else:
        print("Provide the valid output")
