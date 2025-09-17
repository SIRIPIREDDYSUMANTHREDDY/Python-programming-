def climb_stairs(n):
    if n <= 2:
        return n
    return climb_stairs(n-1) + climb_stairs(n-2)

n = 8
print("Number of distinct ways:", climb_stairs(n))
