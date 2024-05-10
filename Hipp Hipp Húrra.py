def celebrate_birthday(name, age):
    for _ in range(age):
        print(f'Hipp hipp hurra, {name}!')

# Example usage:
name = input().strip()
age = int(input().strip())
celebrate_birthday(name, age)
