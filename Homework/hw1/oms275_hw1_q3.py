def sumSquared(num):
    total = 0
    for i in range(num):
        total += i**2
    return total


def sumSquaredListComp(num):
    return sum([x**2 for x in range(num)])


def sumOddSquares(num):
    total = 0
    for i in range(1, num, 2):
        total += i**2
    return total


def sumOddSquaresListComp(num):
    return sum([i**2 for i in range(1, num, 2)])


def main():
    print(sumSquared(20))
    print(sumSquaredListComp(20))
    print(sumOddSquares(20))
    print(sumOddSquaresListComp(20))
