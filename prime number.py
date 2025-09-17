num=int(input("enter the number: "))
lim=int(num/2)+1
for i in range(2,lim):
    rem=num%i
    if rem==0:
        print("is not a prime number: ",num)
        break
else:
    print("prime number: ",num)
