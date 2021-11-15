def shift(lst, num, direct='left'):
    num = num % len(lst)
    if direct == 'left':
        for i in range(num):
            lst.append(lst.pop(0))
    else:
        for i in range(num):
            lst.insert(0, lst.pop(-1))
    return lst


def main():
    lst = [1, 2, 3, 4, 5, 6]
    shift(lst, 2, 'right')
    print(lst)
