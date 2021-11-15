def primeNumFinder(num):
    if num == 1:
        return None
    for i in range(2, num):
        if num % i == 0:
            return None
    return num


def makeTable():
    lower = int(input("Start number: "))
    while lower < 1:
        print("Start and end must be positive")
        lower = int(input("Start number: "))
    upper = int(input("End number: ")) + 1
    while upper <= lower:
        print("End number must be greater than start number")
        upper = int(input("End number: ")) + 1
    table_str = ""
    max_pad = len(str(upper)) + 1
    for num in range(lower, upper):
        result = primeNumFinder(num)
        if result:
            front_pad = " " * (max_pad - len(str(result)))
            table_str += front_pad + str(result)
            if len(table_str) == max_pad * 10:
                print(table_str)
                table_str = ""
    print(table_str)


makeTable()
