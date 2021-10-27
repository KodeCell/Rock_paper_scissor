import random
print('WELCOME TO THE GAME : ROCK PAPER SCISSOR')
choices = ['rock','paper','scissor']
print('__________________________________________')
while True:


    try:
      user_inp = input('''Enter your move: Rock,Paper,Scissor :  ''').upper()
    except ValueError:
        print('wrong value')
        continue
    pc_inp = random.choice(choices).upper()
    if user_inp == pc_inp:
        print(f"Computer and You chose {user_inp} therefore that's a tie")
    elif user_inp == 'ROCK':
        if pc_inp == 'SCISSOR':
            print(f"Computer chose {pc_inp} you chose {user_inp} hence YOU WIN")
        else:
            print(f"Computer chose {pc_inp} you chose {user_inp} hence YOU LOSE")
    elif user_inp == "PAPER":
        if pc_inp == 'ROCK':
            print(f"Computer chose {pc_inp} you chose {user_inp} hence YOU LOSE")
        else:
            print(f"Computer chose {pc_inp} you chose {user_inp} hence YOU WIN")
    elif user_inp == "SCISSOR":
        if pc_inp == 'ROCK':
            print(f"Computer chose {pc_inp} you chose {user_inp} hence YOU LOSE")
        else:
            print(f"Computer chose {pc_inp} you chose {user_inp} hence YOU WIN")
    else:
        print('That is not a valid input check your spelling!!')
        break

    play_again = input('DO you wish to play again? : (y/n)  ').upper()
    if play_again != 'Y':
        break









