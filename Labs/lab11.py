from LinkedBinaryTree import *
from ArrayQueue import *


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


def bt_even_sum(root):
    if not root.left and not root.right and root.data % 2 == 0:
        return root.data
    elif not root.left and not root.right:
        return 0
    if root.data % 2 == 0:
        return root.data + bt_even_sum(root.right) + bt_even_sum(root.left)
    else:
        return bt_even_sum(root.right) + bt_even_sum(root.left)


def bt_contains(root, val):
    if root.data == val:
        return True
    if not root.right and not root.left:
        return False
    if root.right and root.left:
        return bt_contains(root.right, val) or bt_contains(root.left, val)
    elif root.right:
        return bt_contains(root.right, val)
    else:
        return bt_contains(root.left, val)


def is_full(root):
    if not root.left and not root.right:
        return True
    if root.left and root.right:
        return is_full(root.left) and is_full(root.right)
    else:
        return False


def invert_bt(root):
    if not root:
        return
    root.left, root.right = root.right, root.left
    invert_bt(root.left)
    invert_bt(root.right)


def invert_bt_iter(root):
    queue = ArrayQueue()
    queue.enqueue(root)
    while not queue.is_empty():
        node = queue.dequeue()
        node.left, node.right = node.right, node.left
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)


def main():
    root = Node(1)
    my_tree = LinkedBinaryTree(root)
    my_tree.root.left = Node(2)
    my_tree.root.right = Node(3)
    my_tree.root.left.left = Node(4)
    my_tree.root.left.right = Node(5)
    my_tree.root.right.left = Node(6)
    my_tree.root.right.right = Node(7)
    # my_tree.root.right.right.right = Node(8)
    invert_bt_iter(my_tree.root)
    for i in my_tree:
        print(i, end=' ')


main()
