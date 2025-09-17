arr =int(input("enter the array values: "))
unique_arr = []
for num in arr:
    if num not in unique_arr:
        unique_arr.append(num)
print("duplicate array =", unique_arr)
