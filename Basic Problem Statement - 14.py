'''Today coding questions are
Diamond star Pattern/ Sandglass Star Pattern
 *
 ***
 *****
 *******
 *********
 ***********
 ************
 ***********
 *********
 *******
 *****
 ***
 *'''

``
n=5 
for i in range(n):
    for j in range(i):
        print("*",end=" ")
    print("* ")
for i in range(n):
    for j in range(i,n-1):
        print("*",end=" ")
    print("* ")
