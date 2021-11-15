from ArrayQueue import *
from ArrayStack import *
from math import factorial


def permutations(lst):
    """
    :param lst: list
    :return: list
    """
    queue = ArrayQueue()
    stack = ArrayStack()
    total_lst = factorial(len(lst))
    for i in range(1, total_lst+1):
        if total_lst % i+1 == 0:
            val = i - 1
        else:
            val = (i % len(lst)) - 1
        queue.enqueue(lst[val])
    for i in range(1):
        pass
    while total_lst != 0:
        current_lst = queue.dequeue()
        current_vals = stack.pop()


def main():
    permutations([1, 2, 3])


main()
