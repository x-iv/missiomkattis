# Input initial velocity, acceleration, and duration
u, a, t = map(int, input().split())

# Calculate the distance traveled
s = u * t + 0.5 * a * t ** 2

# Print the result
print("{:.9f}".format(s))
