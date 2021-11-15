import random

allowed_sized = [4, 6, 8, 10, 12, 20]
is_allowed = False
size = 0
while not is_allowed:
    size = int(input('How many sides on your dice (4, 6, 8, 10, 12, 20)? '))
    if size in allowed_sized:
        is_allowed = True
        print('\n Thanks, here we go! \n')
    else:
        print('Invalid size, try again.')

double = 0
high_low = 0
evens = 0
odds = 0
sum_size = 0
high_roll = 0
rolls = []
d_1, d_2 = 0, 0
not_snake_eyes = True
while not_snake_eyes:
    d_1, d_2 = random.randint(1, size), random.randint(1, size)
    rolls.append((d_1, d_2))
    result_str = ''
    if (d_1 == size and d_2 == 1) or (d_1 == 1 and d_2 == size):
        result_str += 'High/Low! '
        high_low += 1
    if d_1 % 2 == 0 and d_2 % 2 == 0:
        result_str += 'Evens! '
        evens += 1
    if d_1 % 2 == 1 and d_2 % 2 == 1:
        result_str += 'Odds! '
        odds += 1
    if d_1 + d_2 == size:
        result_str += 'Sum value is size value! '
        sum_size += 1
    if d_1 == d_2:
        result_str += 'Doubles! '
        double += 1
        if d_1 == size:
            result_str += 'High Roll! '
            high_roll += 1
        if d_1 == 1 and d_2 == 1:
            result_str += 'Snake Eyes'
            not_snake_eyes = False

    print('die #1 is *', str(d_1), '* and die #2 is *', str(d_2), '* ', result_str)


print('You finally got snake eyes on roll # ', str(len(rolls)))
print('Along the way you rolled DOUBLES ', str(double), ' times. (', str(round((double/len(rolls))*100, 2)),
      '% of all rolls were doubles)')
print('Along the way you rolled TWO HIGH VALUES ', str(high_roll), ' times. (', str(round((high_roll/len(rolls))*100,
                                                                                          2)),
      '% of all rolls were two high values)')
print('Along the way you rolled TWO EVENS ', str(evens), ' times. (', str(round((evens/len(rolls))*100, 2)),
      '% of all rolls were evens)')
print('Along the way you rolled TWO ODDS ', str(odds), ' times. (', str(round((odds/len(rolls))*100, 2)),
      '% of all rolls were two odds)')
print('Along the way you rolled HIGH / LOW ', str(high_low), ' times. (', str(round((high_low/len(rolls))*100, 2)),
      '% of all rolls were high/low)')
print('Along the way you rolled A SUM VALUE ', str(sum_size), ' times. (', str(round((sum_size/len(rolls))*100, 2)),
      '% of all rolls were a sum_value)')
d_1_total, d_2_total = 0, 0
for i in rolls:
    d_1_total += i[0]
    d_2_total += i[1]
print('Average roll for die #1: ', str(round((d_1_total/len(rolls)), 2)))
print('Average roll for die #2: ', str(round((d_2_total/len(rolls)), 2)))
