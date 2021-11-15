def split_parity(lst):
    counter = -1
    for i in range(len(lst)):
        if lst[i] % 2 == 1:
            counter += 1
            cache = lst[i]
            lst[i] = lst[counter]
            lst[counter] = cache
    return lst
