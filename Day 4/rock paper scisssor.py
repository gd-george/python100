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
import random
choice=int(input("Waht do you choose ? type 0 for Rock, 1 for paper and 2 for scissors\n"))

game=[rock, paper, scissors]

print(f"your choice{game[choice]}")

computer=random.randint(0,2)

print(f"computer's choice {game[computer]}")

if (choice==0 and computer==0) or (choice==1 and computer==1) or (choice==2 and computer==2):
    print("its a tie")
elif (choice==0 and computer==2) or (choice==1 and computer==0) or (choice==2 and computer==1):
    print("You win")
else:
    print("you lose")