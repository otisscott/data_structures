def subtree_min_and_max(root):
    if not root:
        return
    left = subtree_min_and_max(root.left)
    right = subtree_min_and_max(root.right)
    tup = (root.data, root.data)
    if left:
        if left[1] > tup[1]:
            tup = (tup[0], left[1])
        if left[0] < tup[0]:
            tup = (left[0], tup[1])
    if right:
        if right[1] > tup[1]:
            tup = (tup[0], right[1])
        if right[0] < tup[0]:
            tup = (right[0], tup[1])
    return tup


def min_and_max(bin_tree):
    if bin_tree.is_empty():
        raise Exception('Passed binary tree is empty')
    return subtree_min_and_max(bin_tree.root)

