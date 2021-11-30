from LinkedBinaryTree import *
from oms275_hw7_q1 import min_and_max
from oms275_hw7_q3 import is_height_balanced


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
    my_tree.root.left.right = Node(1)
    print(min_and_max(my_tree))
    print(my_tree.leaves_list())
    print(is_height_balanced(my_tree))


main()
