"""
Given N integers, print their sum.
input:
5
1 2 3 4 5
"""

n = int(input())
a = list(map(int, input().split()))
print(sum(a))
