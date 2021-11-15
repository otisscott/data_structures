def primeNumFinder(num):
    if num == 1:
        return "1 is technically not a prime number"
    for i in range(2, num):
        if num % i == 0:
            return str(num) + " is not prime number."
    return str(num) + " is a prime number!"


def main():
    for num in range(1, 1001):
        print(primeNumFinder(num))


main()
