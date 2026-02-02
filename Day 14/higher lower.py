from game_data import data
from art import *
import random


def random_people():
    global A
    global B
    A= random.choice(data)
    B= random.choice(data)
    while A == B:
        B=random.choice(data)

score = 0

random_people()

play=True
while play:
    print("\n"*10)
    print(logo)
    print(f"Your current score is: {score} 💪")
    print (f"Comppare A: {A['name']}, a {A['description']}, from {A['country']}")
    print(vs)
    print (f"Comppare B: {B['name']}, a {B['description']}, from {B['country']}")
    print('')
    choice = input("Who has more followers? A or B: ").upper()

    if (A['follower_count'] > B['follower_count'] and choice == 'A') or (B['follower_count'] > A['follower_count'] and choice == 'B'):
        score+=1
    else:
        play=False

    if B['follower_count'] > A['follower_count']:
        A=B
        B=random.choice(data)
    else:
        B=random.choice(data)

print("\n"*20)
print(logo)
print(f"Sorry that's wrong. Final Score: {score} 🤭")