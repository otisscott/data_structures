from LinkedBinaryTree import *
from oms275_hw7_q1 import min_and_max
from oms275_hw7_q3 import is_height_balanced
from oms275_hw7_q5 import create_expression_tree, prefix_to_postfix


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        if left is not None:
            self.left.parent = self
        self.right = right
        if right is not None:
            self.right.parent = self
        self.parent = None


def main():
    root = Node(3)
    my_tree = LinkedBinaryTree(root)
    my_tree.root.left = Node(2)
    my_tree.root.left.left = Node(9)
    my_tree.root.left.left.left = Node(5)
    my_tree.root.left.left.right = Node(1)
    my_tree.root.right = Node(7)
    my_tree.root.right.left = Node(8)
    my_tree.root.right.right = Node(4)
    print(min_and_max(my_tree))
    print(my_tree.leaves_list())
    print(is_height_balanced(my_tree))
    for i in my_tree.iterative_inorder():
        print(i, end=' ')
    my_prefix_tree = create_expression_tree('* 2 + - 15 6 4')
    test_root = my_prefix_tree.root
    print('\n')
    print(prefix_to_postfix('* 2 + - 15 6 4'))


main()
