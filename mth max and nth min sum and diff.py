num = input("Enter the elements separated by space: ")
array = []
parts = num.split()
for p in parts:
    array.append(int(p))
array.sort()
print(array)
M = int(input("Enter value of M (for maximum): "))
N = int(input("Enter value of N (for minimum): "))
mth_max = array[-M]      # last Mth element
nth_min = array[N-1]    # print results
print(M, "th Maximum Number =", mth_max)
print(N, "th Minimum Number =", nth_min)
print("Sum =", mth_max + nth_min)
print("Difference =", mth_max - nth_min)
