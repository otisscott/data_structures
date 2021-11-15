import math


def factors(num):
    rev_lst, lst = [], []
    num = int(num)
    for i in range(1, math.ceil(math.sqrt(num))):
        if num % i == 0:
            if num / i == i:
                lst.append(i)
            else:
                lst.append(i)
                rev_lst.append(int(num / i))
    final_lst = lst + rev_lst[::-1]
    for j in final_lst:
        yield j


def main():
    for h in factors(1000):
        print(h)
