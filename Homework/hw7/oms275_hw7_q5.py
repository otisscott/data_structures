from LinkedBinaryTree import *


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.parent = None
        self.left = left
        if self.left is not None:
            self.left.parent = self
        self.right = right
        if self.right is not None:
            self.right.parent = self


def create_exp_tree_subexpression(exp_str, start_pos):
    current = Node(exp_str[start_pos])
    start_pos += 1
    if exp_str[start_pos] < '0':
        nested = create_exp_tree_subexpression(exp_str, start_pos)
        current.left = nested[0]
        current.right = Node(int(exp_str[nested[1]]))
        start_pos = nested[1]
    elif exp_str[start_pos+1] < '0':
        current.left = Node(int(exp_str[start_pos]))
        nested = create_exp_tree_subexpression(exp_str, start_pos+1)
        current.right = nested[0]
    else:
        current.left = Node(int(exp_str[start_pos]))
        current.right = Node(int(exp_str[start_pos+1]))
        start_pos += 2
    return current, start_pos


def create_expression_tree(prefix_exp_str):
    exp_list = prefix_exp_str.split(' ')
    exp_tree = LinkedBinaryTree(Node(exp_list[0]))
    current = exp_tree.root
    ind = 1
    while ind < len(exp_list):
        if exp_list[ind].isdigit():
            current.left = Node(int(exp_list[ind]))
            ind += 1
        elif exp_list[ind] < '0':
            if current.left:
                nested = create_exp_tree_subexpression(exp_list, ind)
                current.right = nested[0]
                ind += nested[1]
            else:
                nested = create_exp_tree_subexpression(exp_list, ind)
                current.left = nested[0]
                ind += nested[1]
    return exp_tree


def prefix_to_postfix(prefix_exp_str):
    prefix_tree = create_expression_tree(prefix_exp_str)
    res = ''
    for i in prefix_tree.postorder():
        res += str(i.data) + ' '
    return res[:-1]


