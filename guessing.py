import random


def hi_low_game():
  number = random.randint(1,100)
  count = 0
  play_game = True
  
  print("I'm thinking of a number between 1 and 100")
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")

  if level == 'easy':
    count = 10
  elif level == 'hard':
    count = 5

  while play_game:
    print(f"you have {count} attempts remaing to guess the number")
    guess = int(input("Make a guess: "))
    if guess == number:
      print(f"you guess the correct number it was {number}")
      play_game = False
    elif count < 2:
      print("You've run out of guesses, you lose")
      play_game = False
    elif guess < number:
      print("Too low")
      print("Guess again")
      count-= 1
    elif guess > number:
      count-= 1
      print("Too high")
      print("Guess again")

hi_low_game()