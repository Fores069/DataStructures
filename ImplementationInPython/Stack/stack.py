from collections import deque

stack = deque()
for i in range(5, 0, -1):
    stack.appendleft(i)
print(stack)
for i in range(0, 3):
    stack.popleft()

print(stack)