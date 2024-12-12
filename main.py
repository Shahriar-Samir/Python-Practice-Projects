# options
# game running
# player
# computer
# play again
# thanking

import random


options = ('rock','paper','scissors')


playing = True

while playing:
      player = None
      computer = random.choice(options)
      while player not in options:
          player = input('Enter a value:').lower()
      print(f"you: {player}")
      print(f"computer: {computer}")
      if player == computer:
          print("It's a tie!")
      elif player == "paper" and computer == "rock":
          print("You win!")
      elif player == "rock" and computer == "scissors":
          print("You win!")
      elif player == "scissors" and computer == "paper":
          print("You win!")
      else:
          print("You lose!")
      if input('Want to play again? (y/n):').lower() == "n":
          playing = False

print("Thanks for playing!")



