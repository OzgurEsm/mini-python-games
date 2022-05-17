import random

def guess_the_number(n):
    n = int(n)
    print("Let's go , Guess The Number")
    random_number = random.randint(0,n)
    
    number_of_guesses = 0 
    
    while True :
        guess = int(input(f'Guess a number between 0 and {n}: '))
        number_of_guesses += 1
        
        if guess == random_number:
                print(f'Well done, the number is : {random_number} , it took you {number_of_guesses} times to guess')
                break
        elif guess < random_number:
                print('Go higher!')
        else:
                print('Go lower!')