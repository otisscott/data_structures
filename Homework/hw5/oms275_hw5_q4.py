from ArrayStack import *


class Queue:
    def __init__(self):
        self.stack = ArrayStack()
        self.helper = ArrayStack()

    def __len__(self):
        return len(self.stack)

    def is_empty(self):
        return self.stack.is_empty()

    def enqueue(self, elem):
        while len(self) > 0:
            self.helper.push(self.stack.pop())
        self.stack.push(elem)
        while len(self.helper) > 0:
            self.stack.push(self.helper.pop())

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.stack.pop()
