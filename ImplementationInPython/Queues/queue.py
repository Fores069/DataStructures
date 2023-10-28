from collections import deque

queue = deque([1, 3, 5, 6])
queue.insert(1, 2)
queue.insert(3, 4)
queue.appendleft(0)
queue.appendleft(-1)
queue.append(7)
copy_of_the_queue = queue.copy()
print(copy_of_the_queue)
copy_of_the_queue.append(100)
queue.extend([7, 8, 9])
queue.extendleft([-2, -3, -4])
queue.remove(7)
print(queue)
print(copy_of_the_queue)
queue.clear()
print(queue)


# FIFO
fifo_queue = deque()
fifo_queue.appendleft(1)
fifo_queue.pop()

fifo_queue.append(2)
fifo_queue.popleft()

# LIFO

lifo_queue = deque()
lifo_queue.append(1)
lifo_queue.pop()

lifo_queue.appendleft(3)
lifo_queue.popleft()

