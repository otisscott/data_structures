# a
def find_duplicates(lst):
    num_dict = {}
    for i in lst:
        if i in num_dict:
            num_dict[i] += 1
        else:
            num_dict[i] = 1
    return [key for key, value in num_dict.items() if value > 1]
