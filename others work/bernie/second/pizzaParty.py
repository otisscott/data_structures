budget = int(input("Enter the budget for your party: "))
slice_cost = float(input("Cost per slice of pizza: "))
pie_cost = float(input("Cost per whole pizza pie (8 slices): "))
attendance = int(input("How many people will be attending your party? "))
num_total_slices = 0
for i in range(1, attendance + 1):
    num_desired = int(input("Enter the number of slices for person #" + str(i) + ": "))
    while num_desired < 0:
        print('Not a valid entry, try again!')
        num_desired = int(input("Enter the number of slices for person #" + str(i) + ": "))
    num_total_slices += num_desired

num_pies = num_total_slices // 8
num_slices = num_total_slices % 8
total_cost = (num_pies * pie_cost) + (num_slices * slice_cost)
price_difference = budget - total_cost
if price_difference < 0:
    print("Your order cannot be completed \nYou would need to purchase " + str(num_pies) + " pies and " + str(
        num_slices) + "slices \nThis would put you over budget by " + str(round(abs(price_difference), 2)))
else:
    print("You should purchase " + str(num_pies) + "pies and " + str(num_slices) + "slices")
    print("Your total cost will be: " + str(total_cost))
    if price_difference == 0:
        print('You will have no money left after your order')
    else:
        print('You will still have ' + str(price_difference) + " left after your order")



