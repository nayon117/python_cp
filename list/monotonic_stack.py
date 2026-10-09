"""
Create a stack using a Python list such that you can push and pop elements from the end.
a= [2,1,5,3,4]
"""

a = list(map(int, input().split()))
stack = []

for x in a:
    stack.append(x)

stack.pop()
stack.append(8)

print(*stack)
