import random
import art

print (art.logo)


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) == 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 😒"
    elif c_score == 0:
        return "you lost, computer has a blackjack 💔"
    elif u_score == 0 or u_score == 21:
        return "Winner Winner Chicken Dinner 🍗"
    elif u_score > 21:
        return "you went over 21 you loose 🥲"
    elif c_score > 21:
        return "computer went over YOU WIN!! 🤭"
    elif u_score > c_score:
        return "YOU WIN!!😍"
    else:
        return "YOU LOOSE!!🤦‍♂️"

def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your card: {user_cards} current score: {user_score}")
        print(f"Computer card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal=input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print (f"your final score: {user_score}, computer final score: {computer_score}")
    print(compare(user_score, computer_score))



while input("\ndo you wana play BLACK JACK: ") == "y":
    print("\n" * 20)
    play_game()








