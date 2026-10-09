"""
rotate list by 2 in right
a= [1,2,3,4,5]
"""

a = list(map(int, input().split()))
b = a.copy()

ind = len(a) - 2

a = a[0:ind]
b = b[ind:]

b.extend(a)
print(*b)
