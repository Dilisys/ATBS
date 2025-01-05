import random, sys, time

print('WELCOME TO THE WORLD ROCK, PAPER, SCISSORS CHAMPIONSHIP')
print('Please input your name, Champion:')
player_name = input()

wins = 0
losses = 0
ties = 0

print(player_name + ' VS. MONTY, THE MOST POWERFUL SUPERCOMPUTER IN THE WORLD')
time.sleep(2)
print('Good luck, ' + player_name + '!')
time.sleep(1)

while True: # Main game loop
    print('%s wins, %s losses, %s ties' % (wins, losses, ties))
    while True: # Player input loop
        print('Enter your move: (R)ock, (P)aper, (S)cissors or (Q)uit')
        player_move = input()
        if player_move == 'q':
            sys.exit() # Terminate the game
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break # Break out of the player input loop

        print('Please select a valid move.')

    #Display the player move
    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')

    time.sleep(0.6)
    #Display computer pick
    rand_num = random.randint(1,3)

    if rand_num == 1:
        comp_move = 'r'
        print('. . . ROCK!!!')
    elif rand_num == 2:
        comp_move = 'p'
        print('. . . PAPER!!!')
    elif rand_num == 3:
        comp_move = 's'
        print('. . .SCISSORS!!!')

    time.sleep(0.6)
    
    print('A decisive battle!')

    time.sleep(1.5)
    
    #decide who wins and update tallies
    if player_move == comp_move:
        print('It is a tie!')
        ties += 1
    elif player_move == 'r' and comp_move == 's':
        print(player_name + ' wins!')
        wins += 1
    elif player_move == 'p' and comp_move == 'r':
        print(player_name + ' wins!')
        wins += 1
    elif player_move == 's' and comp_move == 'p':
        print(player_name + ' wins!')
        wins += 1
    elif player_move == 'r' and comp_move == 'p':
        print('COMPUTER wins! YOU lose!')
        losses += 1
    elif player_move == 'p' and comp_move == 's':
        print('COMPUTER wins! YOU lose!')
        losses += 1
    elif player_move == 's' and comp_move == 'r':
        print('COMPUTER wins! YOU lose!')
        losses += 1

    time.sleep(1.0)
