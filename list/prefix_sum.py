"""
a= [2,4,1,3]
expected: [2,6,7,10]
"""

# o(n^2 - worst case)
a = list(map(int,input().split()))

for i in range(1, len(a) + 1):
    print(sum(a[:i]))

# o(n)
prefix_sum = [] 
current_sum = 0

for x in a:
    current_sum += x
    prefix_sum.append(current_sum)

print(prefix_sum)
