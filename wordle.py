import random 
from rich import print #to print in color
import os

words_raw = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'words.txt')
# Apparently this is how your set dir to your script's dir

with open(words_raw,"r") as file:
    words = file.read().split("\n")
    # Have to remove new line char '\n' to make a list with only words
"""if letter in correct position its green
   if not in correct position its yellow
   if not in word at all its white"""

class Wordle:
    # Classes starts with uppercase
    def __init__(self):
        self.word = random.choice(words)
        self.number_of_guesses = 0
        self.guess_dict = {
            0: [" "]*5,
            1: [" "]*5,
            2: [" "]*5,
            3: [" "]*5,
            4: [" "]*5,
            5: [" "]*5,
        }
        
    def draw_board(self):
        # Printing board while joining spaces or letters with '|'
        for guess in self.guess_dict.values():
            print(" | ".join(guess))
            print("="*17)
            
    def get_user_input(self):
        # Get user input and check if its 5 letters and convert to lowercase
        user_guess = input("Write down 5 letter word: ")
        while len(user_guess) != 5:
            user_guess = input('Only 5 letter words: ')
        
        user_guess = user_guess.lower()
               
        for idx,letter in enumerate(user_guess):
            if letter in self.word:
                if letter == self.word[idx]:
                    letter = f'[green]{letter}[/]'
                else:
                    letter = f'[yellow]{letter}[/]'
            self.guess_dict[self.number_of_guesses][idx] = letter
            
        self.number_of_guesses += 1 
        return user_guess   
                    
        
        
    def play(self):
        print("Green means right letter in right place,\nYellow means right letter wrong place, \nWhite means wrong letter")
        while True:
            self.draw_board()
            user_guess = self.get_user_input()
            
            if user_guess == self.word:
                self.draw_board()
                print(f'You Won! It is {self.word}')
                break
            
            if self.number_of_guesses > 5:
                self.draw_board()
                print(f"You Lost! It was {self.word}")
                break