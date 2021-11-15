def remove_all_evens(lst):
    """
    :param lst:
    :return lst:
    """
    lower, upper = 0, len(lst) - 1
    while lower < upper:
        while lst[lower] % 2 == 1 and lower < upper:
            lower += 1
        while lst[upper] % 2 == 0 and lower < upper:
            upper -= 1
        if lower < upper:
            lst[lower], lst[upper] = lst[upper], lst[lower]
            lower += 1
            upper -= 1
    counter = len(lst)-1
    while lst[counter] % 2 == 0:
        lst.pop()
        counter -= 1
    return lst


def is_sorted(lst, low, high):
    if low+1 == high and lst[low] < lst[high]:
        return True
    else:
        if lst[low] < lst[low+1]:
            return is_sorted(lst, low+1, high)
        else:
            return False


def revPrint(lst, low, high):
    if low > high:
        return
    revPrint(lst, low+1, high)
    print(lst[low], end=" ")


def separateNum(lst):
    lower = 0
    upper = len(lst) - 1
    while lower < upper:
        if lst[lower] % 2 == 0:
            if lst[upper] % 2 == 1:
                lst[lower], lst[upper] = lst[upper], lst[lower]
                upper -= 1
                lower += 1
            else:
                upper -= 1
        else:
            lower += 1
    return lst


def main():
    print(remove_all_evens([2, 3, 5, 2, 16, 13]))
    print(is_sorted([1, 3, 6, 7, 8, 15, 31], 0, 6))
    revPrint([1, 2, 3, 4], 0, 3)
    print('')
    lst = [3, 15, 44, 2, 51, 89, 20]
    print(separateNum(lst))


main()
