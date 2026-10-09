"""
8
1 2 1 3 2 1 4 2
"""

n = int(input())
a = list(map(int, input().split()))

freq = [0] * 1000

for x in a:
    freq[x] += 1

seen = []
for x in a:
    if x not in seen:
        print(f"{x} -> {freq[x]}")
        seen.append(x)


