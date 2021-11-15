lower = int(input("Lowest number: "))
while lower < 0:
    print("Lowest must be 0 or greater")
    lower = int(input("Lowest number: "))
upper = int(input("Highest number: ")) + 1
while upper <= lower + 1:
    print("Highest number must be larger than lowest number!")
    upper = int(input("Highest number: ")) + 1
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
        summation = str(row + column)
        padding = (width - len(summation)) * " "
        sum_str = padding + summation
        row_str += sum_str
    print(row_str)

