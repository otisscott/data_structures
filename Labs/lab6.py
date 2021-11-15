def sum_to(n):
    if n == 0:
        return 0
    else:
        return n + sum_to(n-1)


def product_evens(n):
    if n < 2:
        return 1
    else:
        if n % 2 == 1:
            n -= 1
        return n * product_evens(n - 2)


def find_max(lst, low, high):
    if low == high:
        return lst[low]
    low_val = lst[low]
    prev = find_max(lst, low+1, high)
    if low_val > prev:
        prev = low_val
    return prev


def is_palindrome(palindrome, low, high):
    if low == high:
        return True
    if palindrome[low] == palindrome[high]:
        return is_palindrome(palindrome, low+1, high-1)
    else:
        return False


def binary_search(lst, low, high, val):
    if lst[low] == val:
        return low
    if lst[high] == val:
        return val
    if high == low:
        return None
    mid = low+(high-low)//2
    if lst[mid] > val:
        return binary_search(lst, low, mid, val)
    else:
        return binary_search(lst, mid, high, val)


def split_parity(lst, low, high):
    if low == high:
        return lst
    if lst[low] % 2 != 0 and lst[high] % 2 == 0:
        lst[low], lst[high] = lst[high], lst[low]
    if lst[low] % 2 == 0:
        low += 1
    if lst[high] % 2 != 0:
        high -= 1
    return split_parity(lst, low, high)


def vc_count(word, low, high):
    if low >= high:
        if word[low] in "aeiouAEIOU":
            return (1, 0)
        return (0, 1)
    else:
        prev = vc_count(word, low+1, high)
        if word[low] in "aeiouAEIOU":
            return (prev[0] + 1, prev[1])
        return (prev[0], prev[1]+1)


def main():
    print(sum_to(5))
    print(product_evens(20))
    print(find_max([13, 9, 16, 3, 4, 2], 0, 5))
    print(is_palindrome('racecar', 1, 5))
    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 7, 7))
    print(split_parity([4, -5, 2, 3, -1, -6, 7, 9, 0], 0, 8))


main()
