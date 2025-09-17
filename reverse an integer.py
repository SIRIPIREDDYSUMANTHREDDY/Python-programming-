n=int(input("enter the integer: "))
x=n
r=0
while n>0:
    d=n%10
    r=r*10+d
    n=n//10
print("the reverse integer is: ",r)
