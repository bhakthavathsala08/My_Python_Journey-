import random
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

game = [rock, paper, scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user >= 0 and user <= 2:
    print("User chose: ", game[user])
computer = random.randint(0,2)

print("Computer chose: ",game[computer])

if user < 0 or user > 2:
    print("Invalid choice. You lose!")
elif user == 0 and computer == 2:
    print("You win!")
elif user == 2 and computer == 0:
    print("You lose!")
elif user > computer :
    print("You win!")
elif user < computer :
    print("You lose!")
elif user == computer:
    print("It's a tie!")