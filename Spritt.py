import math
n, x= map(int, input().split())
sum_requests = 0

for _ in range(n):
    requests = int(input())
    sum_requests += requests

if sum_requests <= x:
    print("Jebb")
else:
    print("Neibb")
