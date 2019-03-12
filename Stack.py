from collections import deque

class Stack():
    def __init__(self):
        self.stack = deque()
    
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]
        
        
AStack = Stack()
AStack.push("Mon")
AStack.push("Tue")
print(AStack.pop())
AStack.push("Wed")
AStack.push("Thu")
print(AStack.pop())
print(AStack.peek())