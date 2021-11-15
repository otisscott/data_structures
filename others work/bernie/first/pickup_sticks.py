num_sticks = 0
allowed_size = False
while not allowed_size:
    num_sticks = int(input('How many sticks (10-1000)? '))
    if num_sticks > 1000:
        print("Sorry that's too many sticks. Try again")
    elif num_sticks < 10:
        print("Sorry that's too few sticks. Try again")
    else:
        allowed_size = True
        print("Great let's play ... \n")
player_num = 1
while num_sticks > 0:
    print('Turn: Player ', str(player_num))
    print('There are ', str(num_sticks), ' on the table.')
    pick = 0
    allowed_pick = False
    while not allowed_pick:
        pick = int(input('How many sticks do you want to take (1, 2, or 3)? '))
        if 1 <= pick <= 3:
            allowed_pick = True
    num_sticks -= pick
    if num_sticks <= 0:
        print('There are no sticks left on the table! Game over.')
        if player_num == 1:
            print('Player 2 wins!')
        else:
            print('Player 1 wins!')
    player_num = 1 if player_num == 2 else 2



