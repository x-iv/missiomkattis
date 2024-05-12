B_bottles = int(input())
L_bottles = int(input())
if B_bottles == 0 or L_bottles == 0:
    print(0)
elif B_bottles == L_bottles:
    print(B_bottles+L_bottles)
elif B_bottles < L_bottles :
    print(B_bottles * 2)
elif B_bottles > L_bottles:
    print(L_bottles * 2)
