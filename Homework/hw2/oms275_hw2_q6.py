def two_sum(srt_lst, target):
    differences = {}
    for i in range(len(srt_lst)):
        if srt_lst[i] in differences:
            return differences[srt_lst[i]], i
        difference = target - srt_lst[i]
        differences[difference] = i
    return None


def main():
    print(two_sum([-2, 7, 11, 15, 20, 21], 22))
