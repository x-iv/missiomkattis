import math
N = int(input())
joints = N - 1
whole_rod = 0

for _ in range(N):
    len = int(input())
    whole_rod += len

print(whole_rod - joints*1)
