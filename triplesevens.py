# Read input
n = int(input())
wheels = [set(map(int, input().split())) for _ in range(3)]

# Check if all wheels contain the digit 7
if 7 in wheels[0] and 7 in wheels[1] and 7 in wheels[2]:
    print(777)
else:
    print(0)
