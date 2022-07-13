import random


def rock_paper_scissors():
    print("Let's Play: Rock,Paper,Scissors")
    
    r = 'rock'
    p = 'paper'
    s = 'scissors'
    options = [r,p,s]
    
    user_input = input(f"Write your choice; {r}, {p}, {s}: ")
    user_input = user_input.lower()
    computer_input = random.choice(options)
    if user_input not in options:
        print("Invalid choice, Write again please")
        return 
    
    print(f'You picked: {user_input} and Computer picked: {computer_input}')
    
    if user_input == computer_input:
        print("It's a tie!, Choose again!")
        return rock_paper_scissors()
    elif user_input == r and computer_input == s:
        print("Rock smashes scissors!: You won!") 
    elif user_input == s and computer_input == p:
        print("Scissors shred paper!: You won!")
    elif user_input == p and computer_input == r:
        print("Paper covers rock!: You won!")
    elif user_input == s and computer_input == r:
        print("Rock smashes scissors!: You lost!" )
    elif user_input == p and computer_input == s:
        print("Scissors shred paper!: You lost!")
    elif user_input == r and computer_input == p:
        print("Paper covers rock!: You lost!")
    