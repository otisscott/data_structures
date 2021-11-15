def primeNumFinder(num):
    for i in range(2, num):
        if num % i == 0:
            return None
    return num


def main():
    lower = int(input("Start number: "))
    while lower < 1:
        print("Start and end must be positive")
        lower = int(input("Start number: "))
    upper = int(input("End number: ")) + 1
    while upper <= lower:
        print("End number must be greater than start number")
        upper = int(input("End number: ")) + 1
    for num in range(lower, upper):
        if primeNumFinder(num):
            print(primeNumFinder(num))


main()
