a=()
l=[]
n=int(input("enter the limit: "))
for i in range(0,n):
    item=int(input("enter the element: "))
    l.append(item)
a=a+tuple(l)
print("tuple: ",a)
