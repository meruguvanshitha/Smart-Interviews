

S=input()
ans=0
for i in range(len(S)-1,0,-1):
    if S[:i] == S[-i:]:
        ans=i
        break
print(ans)