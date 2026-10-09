"""
remove duplicates 
a= [1,2,2,3,3,3,4]
"""

a = list(map(int,input().split()))
ans = []

for x in a:
    if x not in ans:
        ans.append(x)

print(ans)
