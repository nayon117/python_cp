"""
6
10 5 10 8 3 8
"""

n = int(input())
a = list(map(int, input().split()))

largest = max(a)

sec_largest = float("-inf")
for i in range(len(a)):
    if a[i] > sec_largest and a[i] < largest:
        sec_largest = a[i]

print(sec_largest)  

