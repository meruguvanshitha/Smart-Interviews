

S,T = input().split()
if T==S[:len(T)]and T==S[-len(T):]:
    print("Yes")
else:
    print("No")