positive_sum = 0
positive_count = 0
negative_sum = 0
negative_count = 0
print("Enter -1 to exit")
while True:
    num = int(input("Enter a number: "))
    if num == -1:
        break
    if num > 0:
        positive_sum += num
        positive_count += 1
    elif num < 0:
        negative_sum += num
        negative_count += 1
if positive_count > 0:
    avg_positive = positive_sum
else:
    avg_positive = 0

if negative_count > 0:
    avg_negative = negative_sum
else:
    avg_negative = 0
print("Average positive number is:", avg_positive)
print("Average negative number is:", avg_negative)
