from ArrayStack import *


class MaxStack:
    def __init__(self):
        self.data = ArrayStack()
        self.max_val = (0, 0)

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return self.data.is_empty()

    def push(self, elem):
        print(self.max_val)
        if elem > self.max_val[0]:
            res = (elem, self.max_val[0])
            self.data.push(res)
            self.max_val = (elem, self.max_val[0])
        elif elem > self.max_val[1]:
            res = (elem, self.max_val[0])
            self.data.push(res)
            self.max_val = (self.max_val[0], elem)
        else:
            res = (elem, self.max_val)
            self.data.push(res)

    def top(self):
        return self.data.top()[0]

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        popped = self.data.pop()
        if popped[0] == self.max_val[0]:
            self.max_val = (popped[1], popped[1]-1)
        return popped[0]

    def max(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.max_val[0]


def main():
    maxS = MaxStack()
    maxS.push(3)
    maxS.push(1)
    maxS.push(6)
    maxS.push(4)
    print(maxS.max())
    print(maxS.pop())
    print(maxS.pop())
    print(maxS.max())
