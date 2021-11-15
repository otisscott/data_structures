from ArrayList import *
from ArrayStack import *


def stack_sum(s):
    """
    :param s: ArrayStack
    :return type: int
    """
    sum_stack = 0
    if len(s) == 1:
        return s.top()
    else:
        popped = s.pop()
        sum_stack += popped
        sum_stack += stack_sum(s)
        s.push(popped)
    return sum_stack


def eval_prefix(exp_str):
    """
    :exp_str type: str
    :return type: int
    """
    exp_lst = exp_str.split()
    my_stack = ArrayStack()
    for i in range(len(exp_lst)-1, -1, -1):
        if exp_lst[i].isdigit():
            my_stack.push(int(exp_lst[i]))
        else:
            num1 = my_stack.pop()
            num2 = my_stack.pop()
            if exp_lst[i] == '+':
                my_stack.push(num2 + num1)
            elif exp_lst[i] == '-':
                my_stack.push(num1 - num2)
            elif exp_lst[i] == '/':
                my_stack.push(num1 / num2)
            elif exp_lst[i] == '*':
                my_stack.push(num2 * num1)
    return my_stack.pop()


def flatten_list(lst):
    """
    :param lst: list
    :return: None
    """
    my_stack = ArrayStack()
    for i in range(len(lst)-1, -1, -1):
        if isinstance(lst[i], list):
            pass


def main():
    s = ArrayStack()
    s.push(-8)
    s.push(-5)
    s.push(10)
    s.push(9)
    s.push(-7)
    s.push(6)
    s.push(5)
    s.push(-14)
    s.push(1)
    print(stack_sum(s))
    prefix_str = "+ * 6 3 * 8 4"
    print(eval_prefix(prefix_str))


main()
