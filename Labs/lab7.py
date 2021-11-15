def nested_sum(lst):
    """
    :param lst:
    :return int:
    """
    num_sum = 0
    for i in lst:
        if isinstance(i, list):
            num_sum += nested_sum(i)
        else:
            num_sum += i
    return num_sum


def nested_depth_level(lst):
    """
    :param lst:
    :return int:
    """
    max_depths = []
    max_depth = 1
    for i in lst:
        if isinstance(i, list):
            max_depths.append(nested_depth_level(i))
    if max_depths:
        max_depth += max(max_depths)
        return max_depth
    return 1


def deep_reverse(lst):
    """
    :param lst:
    :return None:
    """
    lst.reverse()
    for i in lst:
        if isinstance(i, list):
            deep_reverse(i)


def main():
    lst1 = [[1, 2], 3, [4, [5, 6, [7], 8]]]
    print(nested_sum(lst1))
    lst2 = [[1, 2], 3, [4, [5, 6, [7], 8]], [[[[9]]]]]
    lst3 = [[1, 2], 3, [4, [5, 6, [7], 8]]]
    lst4 = [1, 2]
    print(nested_depth_level(lst2))
    print(nested_depth_level(lst3))
    print(nested_depth_level(lst4))
    deep_reverse(lst2)
    print(lst2)


main()
