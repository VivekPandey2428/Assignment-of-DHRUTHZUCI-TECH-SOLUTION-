lst = [int(item) for item in input().split()] 
ans=0
for i in lst:
    ans=ans^i

print(ans)