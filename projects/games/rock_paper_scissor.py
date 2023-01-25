import random
print('Welcome to Rock Paper Scissor Game\n')
user=int(input('Enter 0 for rock, 1 for paper, and 2 for scissor: '))
computer=random.randint(0,2)
list_of_choices=['''
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
    ''',
'''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|              
    ''',
'''
          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ /
|___/\___|_|___/___/\___/|_|  |___/
                                       
    ''',user,computer
    ]

for i in range(3,5):
    if(i==3):
        current='You'
    else:
        current='computer'
    
    if(list_of_choices[i]==0):
        print(f"{current} choose: {list_of_choices[0]}")
    elif(list_of_choices[i]==1):
        print(f"{current} choose: {list_of_choices[1]}")   
    elif(list_of_choices[i]==2):
        print(f"{current} choose: {list_of_choices[2]}")

if(computer==3 and user==0):
    print('Congratulations! You Won')        
elif(computer>user):
    print('You Loose!')
elif(computer==0 and user==1):
    print('Congratulations! You won')
elif(user==2 and computer==2):
    print('Congratulation! You won.')        
elif(computer<user):
    print('You Loose!')    
elif(computer==user):
    print('It\'s a draw') 
else:
    print('Invalid input.')       