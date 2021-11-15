def fibs(n):
    n_1, n_2 = 1, 1
    for i in range(n):
        yield n_1
        n_1, n_2 = n_2, n_1 + n_2


def main():
    for i in fibs(8):
        print(i)
