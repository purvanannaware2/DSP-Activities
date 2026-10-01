# Task Management using Stack and Queue

from collections import deque

# Stack
stack = []

stack.append("Task 1")
stack.append("Task 2")
stack.append("Task 3")

print("Stack Tasks:")
print(stack)

print("Completed from Stack:", stack.pop())
print("Remaining Stack Tasks:", stack)


# Queue
queue = deque()

queue.append("Task 1")
queue.append("Task 2")
queue.append("Task 3")

print("\nQueue Tasks:")
print(list(queue))

print("Completed from Queue:", queue.popleft())
print("Remaining Queue Tasks:", list(queue))