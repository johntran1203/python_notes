rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

computer = random.randint(0,2)
player1 = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors "))


if computer == player1:
  print("TIE GAME!!", computer, player1)
elif computer == 0 and player1 == 1:
  print(f"player1 wins {paper} beat {rock}")
elif computer == 0 and player1 == 2:
  print(f"computer wins {rock} beat {scissors}")
elif computer == 1 and player1 == 0:
  print(f"Player 1 wins {paper} beats {rock}" )
elif computer == 1 and player1 == 2:
  print(f"player 1 wins {scissors} beat {paper}")
elif computer == 2 and player1 == 1:
  print(f"computer wins {scissors} beat {paper}")
elif computer == 2 and player1 == 0:
  print(f"player1 wins {rock} beats {scissors}")
else:
  print("something is wronf", computer, player1)

  
