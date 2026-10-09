"""
1 0 3 0 5 0 2
"""

a = list(map(int, input().split()))
b = []
for x in a:
    if x == 0:
        b.append(x)
        a.remove(x)

a.extend(b)
print(*a)

# alternative
a = list(map(int, input().split()))
b = [x for x in a if x!= 0]
b += [0] * (len(a) - len(b))

print(*b)
