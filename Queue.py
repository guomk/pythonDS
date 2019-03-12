from collections import deque

class Queue():
    def __init__(self):
        self.queue = deque()

    def enque(self, item):
        self.queue.appendleft(item)

    def deque(self):
        if not self.queue:
            return 'Invalid'
        return self.queue.pop()

    def peek(self):
        if not self.queue:
            return 'Invalid'
        return self.queue[-1]

AQueue = Queue()
AQueue.enque(1)
AQueue.enque(2)
AQueue.enque(3)
print(AQueue.peek())
print(AQueue.deque())
print(AQueue.peek())
print(AQueue.deque())
print(AQueue.deque())
print(AQueue.deque())