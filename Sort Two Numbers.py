line = input()
a, b = map(int, line.split())
if a < b:
    print(a, b)
else:
    print(b, a)
