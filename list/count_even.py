"""
Given an array, count how many elements are even.
6
1 4 7 8 10 13
"""

n = int(input())
a = list(map(int,input().split()))

cnt = 0
for x in a:
    if x % 2 == 0:
        cnt += 1

print(cnt)

# alternative
print(sum(x%2 ==  0 for x in a))
