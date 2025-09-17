nums = input("Enter numbers separated by space: ")
arr = []
parts = nums.split()
for p in parts:
    arr.append(int(p))
arr.sort()
second_max = arr[-2]
print("Second Maximum Number =", second_max)
