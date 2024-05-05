# Read input
n = int(input())
guests = []
for _ in range(n):
    name, fun = input().split()
    guests.append((name, int(fun)))

# Find the guest with the highest fun value
max_fun = max(guests, key=lambda x: x[1])

# Output the name of the guest with the highest fun value
print(max_fun[0])
