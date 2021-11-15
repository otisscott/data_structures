def primeNumFinder(num):
    for i in range(2, num):
        if num % i == 0:
            return None
    return num


lower = int(input("Lowest number: "))
while lower < 0:
    print("Lowest must be 0 or greater")
    lower = int(input("Lowest number: "))
upper = int(input("Highest number: ")) + 1
while upper <= lower + 1:
    print("Highest number must be larger than lowest number!")
    upper = int(input("Highest number: ")) + 1
wantPrime = input("Would you like to identify Prime numbers in your table? (y/n): ")
validWantPrime = False
if wantPrime == 'y' or wantPrime == 'n':
    validWantPrime = True
while not validWantPrime:
    print("Invalid commend, try again")
    wantPrime = input("Would you like to identify Prime numbers in your table? (y/n): ")
    if wantPrime == 'y' or wantPrime == 'n':
        validWantPrime = True
if wantPrime == 'y':
    width = len(str(upper)) + 4
else:
    width = len(str(upper)) + 3
header = " +  " + (" " * (len(str(upper)) - 2))
divider = "---"
for num in range(lower, upper):
    header += ((width - len(str(num))) * " ") + str(num)
    divider += '-' * width
print(header)
print(divider)
for row in range(lower, upper):
    row_str = str(row) + (len(str(upper)) - len(str(row))) * " " + " |"
    for column in range(lower, upper):
        summation = row + column
        if wantPrime == 'y' and primeNumFinder(summation):
            summation = str(summation) + "p"
        else:
            summation = str(summation)
        padding = (width - len(summation)) * " "
        sum_str = padding + summation
        row_str += sum_str
    print(row_str)

