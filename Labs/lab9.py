import numbers

from ArrayQueue import *


class ArrayDeque:
    INITIAL_CAPACITY = 8

    def __init__(self):
        self.data = make_array(ArrayDeque.INITIAL_CAPACITY)
        self.num_of_elems = 0
        self.front_ind = None
        self.back_ind = None

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return self.num_of_elems == 0

    def first(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.data[self.front_ind]

    def last(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.data[self.back_ind]

    def resize(self, new_size):
        original = self.data()
        new_dequeue = make_array(new_size)
        old_front = self.front_ind
        for ind in range(self.num_of_elems):
            new_dequeue[ind] = original[old_front]
            old_front = (old_front + 1) % len(original)
        self.data = new_dequeue
        self.front_ind = 0
        self.back_ind = self.front_ind + self.num_of_elems - 1

    def enqueue_first(self, elem):
        if self.num_of_elems == len(self.data):
            self.resize(2 * len(self.data))
        if self.is_empty():
            self.data[0] = elem
            self.front_ind = 0
            self.back_ind = 0
            self.num_of_elems = 1
        else:
            self.front_ind = (self.front_ind - 1) % len(self.data)
            self.data[self.front_ind] = elem
            self.num_of_elems += 1

    def enqueue_last(self, elem):
        if self.num_of_elems == len(self.data):
            self.resize(2 * len(self.data))
        if self.is_empty():
            self.data[0] = elem
            self.front_ind = 0
            self.back_ind = 0
            self.num_of_elems = 1
        else:
            self.back_ind = (self.back_ind + 1) % len(self.data)
            self.data[self.back_ind] = elem
            self.num_of_elems += 1

    def dequeue_first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if self.is_empty():
            self.front_ind = None
            self.back_ind = None
        elif self.num_of_elems < len(self.data) // 4:
            self.resize(len(self.data) // 2)
        return value

    def dequeue_last(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self.data[self.back_ind]
        self.data[self.back_ind] = None
        self.back_ind = (self.back_ind - 1) % len(self.data)
        self.num_of_elems -= 1
        if self.is_empty():
            self.front_ind = None
            self.back_ind = None
        elif self.num_of_elems < len(self.data) // 4:
            self.resize(len(self.data) // 2)
        return value


class MeanQueue:
    def __init__(self):
        self.data = ArrayQueue()
        self.total = 0

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return self.data.is_empty()

    def enqueue(self, e):
        if not isinstance(e, numbers.Number):
            raise TypeError('Invalid type, must be int or float')
        self.data.enqueue(e)
        self.total += e

    def dequeue(self):
        if len(self) == 0:
            raise ValueError('queue is empty')
        self.total -= self.first()
        return self.data.dequeue()

    def first(self):
        if len(self) == 0:
            raise ValueError('queue is empty')
        return self.data.first()

    def sum(self):
        return self.total

    def mean(self):
        return self.total / len(self)


class QueueStack:
    def __init__(self):
        self.data = ArrayQueue()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def fast_push(self, item):
        self.data.enqueue(item)

    def fast_pop(self):
        return self.data.dequeue()

    def fast_top(self):
        return self.data.first()

    def push(self, item):
        self.data.enqueue(item)
        i = 0
        while i < len(self.data) - 1:
            temp = self.data.dequeue()
            self.data.enqueue(temp)
            i += 1

    def pop(self):
        i = 0
        while i < len(self) - 1:
            temp = self.data.dequeue()
            self.data.enqueue(temp)
            i += 1
        return self.data.dequeue()

    def top(self):
        i = 0
        while i < len(self) - 1:
            temp = self.data.dequeue()
            self.data.enqueue(temp)
            i += 1
        result = self.data.first()
        temp = self.data.dequeue()
        self.data.enqueue(temp)
        return result


def flatten_list_by_depth(lst):
    """
    :param lst: list
    :return: list
    """
    q = ArrayQueue()
    new_lst = []
    for i in lst:
        q.enqueue(i)
    while not q.is_empty():
        current_item = q.dequeue()
        if isinstance(current_item, list):
            for j in current_item:
                q.enqueue(j)
        else:
            new_lst.append(current_item)
    return new_lst


def genBinary(n):
    """
    :param n: num
    :return: list
    """
    q = ArrayQueue()
    result = []
    q.enqueue('1')
    while n > 0:
        n -= 1
        temp = q.dequeue()
        result.append(temp)
        q.enqueue(temp+'0')
        q.enqueue(temp+'1')
    return result


def main():
    my_dequeue = ArrayDeque()
    my_dequeue.enqueue_last(1)
    my_dequeue.enqueue_last(2)
    my_dequeue.enqueue_last(3)
    my_dequeue.enqueue_first(4)
    my_dequeue.enqueue_first(5)
    my_dequeue.enqueue_first(6)
    print(my_dequeue.dequeue_last())
    print(my_dequeue.dequeue_last())
    print(my_dequeue.dequeue_first())

    my_mean = MeanQueue()
    my_mean.enqueue(5)
    my_mean.enqueue(5)
    my_mean.enqueue(5)
    my_mean.enqueue(5)
    my_mean.enqueue(5)
    print(my_mean.sum())
    print(my_mean.mean())
    my_mean.dequeue()
    print(my_mean.sum())
    print(my_mean.mean())

    my_lst = [[[[0]]], [1, 2], 3, [4, [5, 6, [7]], 8], 9]
    print(flatten_list_by_depth(my_lst))
    print(genBinary(10))

    my_stack = QueueStack()
    my_stack.fast_push(-1)
    my_stack.fast_push(0)
    my_stack.fast_push(3)
    my_stack.fast_push(-1)
    my_stack.fast_push(2)
    my_stack.fast_push(4)
    print(my_stack.pop())
    print(my_stack.top())


main()
