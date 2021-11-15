from ArrayStack import *
from ArrayDeque import *


class MidStack:
    def __init__(self):
        self.stack = ArrayStack()
        self.deque = ArrayDeque()

    def __len__(self):
        return len(self.deque) + len(self.stack)

    def is_empty(self):
        if self.deque.is_empty():
            if self.stack.is_empty():
                return True
        return False

    def push(self, elem):
        self.deque.enqueue_first(elem)
        if len(self) % 2 == 1:
            popped = self.deque.dequeue_last()
            self.stack.push(popped)

    def pop(self):
        if self.is_empty():
            raise Exception('MidStack empty')
        if self.deque.is_empty():
            return self.stack.pop()
        popped = self.deque.dequeue_first()
        if len(self) % 2 == 1 and len(self) != 1:
            self.deque.enqueue_last(self.stack.pop())
        return popped

    def mid_push(self, elem):
        if len(self) % 2 == 0:
            self.stack.push(elem)
        else:
            self.deque.enqueue_last(elem)

    def top(self):
        return self.deque.front_ind


def main():
    midS = MidStack()
    midS.push(2)
    midS.push(4)
    midS.push(6)
    midS.push(8)
    midS.push(10)
    midS.push(12)
    midS.mid_push(12)
    print(midS.pop())
    print(midS.pop())
    print(midS.pop())
    print(midS.pop())
    print(midS.pop())
    print(midS.pop())


main()
