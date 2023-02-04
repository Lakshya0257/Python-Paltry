import random
import os

def game_mode(number,level):
    if(level=='easy'):
        attempts=10
    else:
        attempts=5
    while attempts!=0:
        print(f'Attempts remaining: {attempts}')
        number_guessed=int(input('Guess the number: '))
        if(number==number_guessed):
            return f'Congratulations! You guessed the correct number : {number}'
        elif(number>number_guessed):
            print('You guessed lower than the number, Try again')
            attempts-=1
        else:
            print('You guessed higher than the number, Try again')
            attempts-=1
    return f'You Lost! Number was {number}'   



flag=True
while flag:
    print('Welcome to Game of Number Guessing.\nNumber will be randomly choosen between 1 to 100')
    level=input('Enter the level of your game (easy/hard): ')
    if(level=='easy'):
        print(game_mode(random.randint(1,100),'easy'))
        play_again=(input('Wanna play again? (True/False): '))
        os.system('cls')
        if(play_again=='False'):
            flag=False
    elif(level=='hard'):
        print(game_mode(random.randint(1,100),'hard'))
        play_again=(input('Wanna play again? (True/False): '))
        os.system('cls')
        if(play_again=='False'):
            flag=False
        
    else:
        print('Incorrect Mode! Try Again')
print('Thanks for playing!')            

        
