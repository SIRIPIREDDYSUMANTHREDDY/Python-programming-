# Program to find average of positive and negative numbers

pos_sum = 0
pos_count = 0
neg_sum = 0
neg_count = 0

print("Enter -1 to exit")
while True:
    num = int(input("Enter number: "))
    
    if num == -1:
        break
    
    if num > 0:
        pos_sum += num
        pos_count += 1
    elif num < 0:
        neg_sum += num
        neg_count += 1

# Calculate averages
if pos_count > 0:
    pos_avg = pos_sum / pos_count
else:
    pos_avg = 0

if neg_count > 0:
    neg_avg = neg_sum / neg_count
else:
    neg_avg = 0

print("Average of positive numbers is:", pos_avg)
print("Average of negative numbers is:", neg_avg)
