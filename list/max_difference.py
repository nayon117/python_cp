"""
given an array find maximum difference
5
8 2 10 4 6
"""

n = int(input())
a = list(map(int, input().split()))

diff = max(a) - min(a)
print(diff)
