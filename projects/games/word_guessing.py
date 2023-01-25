import random

def welcome():
    print('''
██     ██  ██████  ██████  ██████       ██████  ██    ██ ███████ ███████ ███████ ███████ ██████  
██     ██ ██    ██ ██   ██ ██   ██     ██       ██    ██ ██      ██      ██      ██      ██   ██ 
██  █  ██ ██    ██ ██████  ██   ██     ██   ███ ██    ██ █████   ███████ ███████ █████   ██████  
██ ███ ██ ██    ██ ██   ██ ██   ██     ██    ██ ██    ██ ██           ██      ██ ██      ██   ██ 
 ███ ███   ██████  ██   ██ ██████       ██████   ██████  ███████ ███████ ███████ ███████ ██   ██ 
    \n\nWelcome to Word Guesser :)''')
    rules()


def rules():
    print('''
    -----------------------------INSTRUCTIONS-------------------------------
    1) A random word will be generated.
    2) Guess a character and find out that word.
    3) For every wrong guess, a life will be detucted.
    
    ALL THE BEST
    ''')

welcome()
flag=True
while flag==True:
    lst=['hello','bye','mouse','river','cat']
    lifeline=['* ' for j in range(5)]
    word=lst[random.randint(0,len(lst)-1)]
    guess=(["_" for i in word])


    while "".join([chr for chr in guess])!=word:
        print('-------------------------------------------')
        print(''.join(i for i in lifeline))
        print("".join([ch for ch in guess]))

        character=input("Guess a letter: ")

        
        if any(i==character for i in word):
            for j in range(0,len(word)):
                if character==word[j]:
                    guess[j]=character
        else:
            print("Not Found")
            lifeline.pop(len(lifeline)-1)
            if len(lifeline)==0:
                guess=word
                print(f"You lost to guess the word\nWord was : {guess}")
        
        if "".join([chr for chr in guess])==word and len(lifeline)!=0:
            print(f'Congratulations! You guessed the word\nWord was : {word}')
    input=(input("Wanna play again? (y/n):"))


    if input=='y':
        flag=True
    else:
        print('Thanks for playing!')
        flag=False    
              
