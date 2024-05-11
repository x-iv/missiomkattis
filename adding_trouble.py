def check_addition(a, b, c):
    return "correct!" if a + b == c else "wrong!"

# Taking input
a, b, c = map(int, input().split())

# Checking addition
result = check_addition(a, b, c)

# Outputting result
print(result)
