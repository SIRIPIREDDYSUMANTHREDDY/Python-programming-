arr = [2, 3, 2, 4, 3, 5, 2]
freq = {}

for x in arr:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

print("Frequencies:", freq)
