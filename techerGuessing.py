from random import randint



# Make function to set difficulty
def difficulty():
  level = input("Choose a difficulty ")
  if level == 'easy':
    return EASY_LEVEL_TURNS
  else:
    return  HARD_LEVEL_TURNS

# Function to check user's guess against actual answer
turns = 0
def check_answer(guess, answer, turns):
  if guess > answer:
    print("To high")
    return turns -1
  elif guess < answer:
    return turns -1
    print("to low")
  else:
    print(f"you got it! the answer was {answer}")

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def game():
  # Choosing a random number between 1 and 100
  print("Welcome to the Number guessing Game!")
  print("I'm thinking of a number between 1 and 100.")

  answer = randint(1,100)
  print(f"the correct answer is {answer}")

  turns = difficulty()


  # repeat the guessing functionalilty if they get it wrong
  guess = 0
  while guess != answer:
    print(f"You have {turns} attemps remaining to guess the number. ")
  # Let the user guess a number
    guess = int(input("Guess a number!? "))
    turns = check_answer(guess, answer, turns)
    if turns  ==0:
      print("you run out of guess")
      return
    


  # track the number of turns and reduce by 1 if they get it wrong


game()