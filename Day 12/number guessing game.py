import random
import art

def compare(num, guess):
    if num == guess:
        return "\nCcrrect Guess 🎊 YOU WIN 🎊"
    elif num < guess:
        return "guess lower ⬇️"
    else:
        return "Guess higher ⬆️"

def play_game():
    print("\n" * 20)
    print(art.logo)
    print("The number is between 1 and 100.")
    num=random.randint(1,100)
   

    mode=input("choose a difficulty: Type E for easy or H for hard\n").lower()

    if mode=="e":
        count=10
    else:
        count=5

    guess_left=count

    for i in range(count):

        print(f"you have {guess_left} guesses left")

        guess=int(input("Make a Guess 🤷 : "))

        result=compare(num,guess)
        print(result)
        if result=="\nCcrrect Guess 🎊 YOU WIN 🎊":
            break
        guess_left-=1
        if guess_left<=0:
            print(f"\nYou ran out of guesses 🥲  YOU LOSE. The number was {num}")

play_again=True

while play_again:
    play_game()
    play_again=input("\nDo you want to play again? (y/n): ").lower()
    if play_again=="n":
        play_again=False

print(art.thanks)

