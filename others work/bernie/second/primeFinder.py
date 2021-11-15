def primeNumFinder(num):
    if num == 1:
        return "1 is technically not a prime number"
    for i in range(2, num):
        if num % i == 0:
            print(str(i) + " is a divisor of " + str(num) + " ... stopping")
            return str(num) + " is not prime number."
        else:
            print(str(i) + " is NOT a divisor of " + str(num) + " ... continuing")
    return str(num) + " is a prime number!"


def main():
    num = int(input("Enter a positive number to test: "))
    print(primeNumFinder(num))


main()
