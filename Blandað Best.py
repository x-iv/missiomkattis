n = int(input())
meat = [input() for _ in range(n)]
if "nautakjot" in meat and "kjuklingur" in meat:
    print("blandad best")
elif "nautakjot" in meat:
    print("nautakjot")
else:
    print("kjuklingur")
