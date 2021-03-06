from ArrayQueue import ArrayQueue


class LinkedBinaryTree:
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

    def __init__(self, root=None):
        self.root = root
        self.size = self.count_nodes()

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def count_nodes(self):
        def subtree_count(root):
            if root is None:
                return 0
            else:
                left_count = subtree_count(root.left)
                right_count = subtree_count(root.right)
                return 1 + left_count + right_count

        return subtree_count(self.root)

    def sum(self):
        def subtree_sum(root):
            if root is None:
                return 0
            else:
                left_sum = subtree_sum(root.left)
                right_sum = subtree_sum(root.right)
                return root.data + left_sum + right_sum

        return subtree_sum(self.root)

    def height(self):
        def subtree_height(root):
            if root.left is None and root.right is None:
                return 0
            elif root.left is None:
                return 1 + subtree_height(root.right)
            elif root.right is None:
                return 1 + subtree_height(root.left)
            else:
                left_height = subtree_height(root.left)
                right_height = subtree_height(root.right)
                return 1 + max(left_height, right_height)

        if self.is_empty():
            raise Exception("Tree is empty")
        return subtree_height(self.root)

    def preorder(self):
        def subtree_preorder(root):
            if root is None:
                pass
            else:
                yield root
                yield from subtree_preorder(root.left)
                yield from subtree_preorder(root.right)

        yield from subtree_preorder(self.root)

    def postorder(self):
        def subtree_postorder(root):
            if root is None:
                pass
            else:
                yield from subtree_postorder(root.left)
                yield from subtree_postorder(root.right)
                yield root

        yield from subtree_postorder(self.root)

    def inorder(self):
        def subtree_inorder(root):
            if root is None:
                pass
            else:
                yield from subtree_inorder(root.left)
                yield root
                yield from subtree_inorder(root.right)

        yield from subtree_inorder(self.root)

    def breadth_first(self):
        if self.is_empty():
            return
        line = ArrayQueue()
        line.enqueue(self.root)
        while not line.is_empty():
            curr_node = line.dequeue()
            yield curr_node
            if curr_node.left is not None:
                line.enqueue(curr_node.left)
            if curr_node.right is not None:
                line.enqueue(curr_node.right)

    def __iter__(self):
        for node in self.breadth_first():
            yield node.data

    def leaves_list(self):
        if self.is_empty():
            return []

        def helper(root):
            if not root:
                return []
            else:
                left = helper(root.left)
                right = helper(root.right)
                if not root.left and not root.right:
                    return left + right + [root.data]
                else:
                    return left + right
        return helper(self.root)

    def iterative_inorder(self):
        cur_node = self.root
        while cur_node:
            if not cur_node.left:
                yield cur_node.data
                cur_node = cur_node.right
            else:
                left = cur_node.left
                while left.right and left.right != cur_node:
                    left = left.right
                if not left.right:
                    left.right = cur_node
                    cur_node = cur_node.left
                else:
                    left.right = None
                    yield cur_node.data
                    cur_node = cur_node.right
