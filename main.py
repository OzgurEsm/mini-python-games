from gtn import guess_the_number
from rps import rock_paper_scissors
from wordle import Wordle
from connect_four import ConnectFour
from tictactoe import TicTacToe

""" Use underscores for readability"""


while True:
    text = """Welcome to Mini Games!
    * (1)Guess The Number
    * (2)Rock,Paper,Scissors
    * (3)wordle
    * (4)ConnectFour
    * (5)Tic Tac Toe
    Select a game by number or 'q' to quit: 
    """
    value = input(text)
    """ input always gives us a string so either change input to int
    or the value to string"""
    if value == "1":
        guess_the_number(input("Enter a number: "))
    elif value == "2":
        rock_paper_scissors()
    elif value == "3":
        game = Wordle()
        game.play()
    elif value == "4":
        game = ConnectFour()
        game.play()
    elif value == "5":
        game = TicTacToe()
        game.play()
    elif value == "q":
        break