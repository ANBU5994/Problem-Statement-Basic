def num (a,b):
    if a>b:
        print (a," is larger")
    elif b>a:
        print(b," is larger")
    else:
        print("both are equal")
    
a=int(input("enter the 1 st mysterious number "))
b=int(input("enter the 2 nd mysterious number  "))

try:
    res=num(a,b)
    print(res)
except:
    print("enter the correct value")


