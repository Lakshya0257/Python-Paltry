import random
import data
import art
import os

def re_run():
    value=input('Wanna Re-Run? (y/n): ')
    if(value=='y'):
        os.system('cls')
        return True
    print('Thanks for using!')    
    return False    


def game():
    print(art.logo)
    flag=True
    score=0
    while flag:
        option_A=random.randint(0,len(data.data)-1)
        option_B=random.randint(0,len(data.data)-1)
        if(option_A==option_B):
            flag=True
        else:
            print(f"Option A: {data.data[option_A]['name']}, {data.data[option_A]['description']} from {data.data[option_A]['country']}\n{art.vs}\nOption B: {data.data[option_B]['name']}, {data.data[option_B]['description']} from {data.data[option_B]['country']}")
            flag=answer_check(input('Enter which has most number of followers: (A/B): '),option_A,option_B)
            if flag:
                score+=1
            os.system('cls')
            print(f'Your score is : {score}')
            
    return re_run()        



def answer_check(option_choosen,option_A,option_B):
    if(data.data[option_A]['follower_count']>data.data[option_B]['follower_count']):
        if(option_choosen=='A'):
            print('Congratulations! You choosen right')
            return True
        else:
            print('Uff! You Lost :(')
            return False
    else:
        if(option_choosen=='B'):
            print('Congratulations! You choosen right')
            return True
        else:
            print('Uff! You Lost :(')
            return False        


flag=True
while flag:
    flag=game()