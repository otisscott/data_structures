def height(root):
    if not root:
        return 0
    return max(height(root.left), height(root.right)) + 1


def is_height_balanced(bin_tree):
    if bin_tree.is_empty():
        raise Exception('Passed bin tree is empty')

    def balanced(root):
        if not root:
            return True
        left = height(root.left)
        right = height(root.right)
        if -1 <= left - right <= 1 and balanced(root.right) and balanced(root.left):
            return True
        return False

    return balanced(bin_tree.root)
