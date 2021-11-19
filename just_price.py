import random2 as rnd
import time

def game_end_bye():
    print('Bye ! ')
    print('Hope you enjoyed the game !')

def replay_game():
    replay = raw_input('Would you like to play another game ? [y/n] ')
    if replay.lower() == 'y':
        game_start()
    else:
        game_end_bye()

def game_start():
    print('Welcome in the Just Price. There are two game modes. ')
    print("1) Tentatives - You have a limited number of trials to find the Just Price")
    print("2) TimeOut - You have a limited time to find the Just Price")
    game_mode = input('Which mode do you want to play? ')
    if game_mode == 2:
        game_mode_timeout()
    elif game_mode == 1:
        game_mode_tentative()

def game_mode_timeout():
    price = rnd.randrange(0, 1000)
    print("Welcome in the TimeOut mode ! ")
    print("In this mode, you have 30 seconds to find the Just Price ! Ready ?")
    print("Let's go !")
    now = time.time()
    timeout = now + 30
    while time.time() < timeout:
        guess = input("Guess the Price : ")
        if guess == price:
            print('Good Job, you guess the price !')
            replay_game()
            break
        elif guess > price:
            print('It is less')
        else:
            print('It is more')
    else:
        print('Time Out !!')
        replay_game()

def game_mode_tentative():
    price = rnd.randrange(0, 100)
    print("Welcome in the Tentatives mode ! ")
    print("In this mode, you have 10 tentatives to find the Just Price !")
    tentative = 0
    while tentative < 10:
        guess = input("Guess the Price : ")
        if guess == price:
            print('Good Job, you guess the price !')
            replay_game()
            break
        elif guess > price:
            print('It is less')
            tentative += 1
            remaining_tentative = 10-tentative
            print("Remaining tentative : {remaining_tentative}".format(remaining_tentative=remaining_tentative))
        else:
            print('It is more')
            tentative += 1
            remaining_tentative = 10-tentative
            print("Remaining tentative : {remaining_tentative}".format(remaining_tentative=remaining_tentative))
    else:
        print("No more tentative. You Lost")
        replay_game()

game_start()