from art import logo
import random


def deal_card():
    '''Picking a new card randomly from the deck.'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    '''Calculting cards score'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(a, b):
    if a == b:
        return "Draw"
    elif b == 0:
        return "You lose, opponent has Blackjack"
    elif a == 0:
        return "You win with a Blackjack"
    elif a > 21:
        return "You went over. You lose"
    elif b > 21:
        return "Opponent went over. You win"
    elif a > b:
        return "You win"
    else:
        return "You lose"


def game():
    print(logo)

    my_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        my_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        my_score = calculate_score(my_cards)
        computer_score = calculate_score(computer_cards)
        computer_first_card = computer_cards[0]

        print(f"Your cards: {my_cards}, current score: {my_score}")
        print(f"Computer's first card: {computer_first_card}")

        if my_score == 0 or computer_score == 0 or my_score > 21:
            is_game_over = True
        else:
            question = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if question == 'y':
                my_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final cards: {my_cards} and score: {my_score}")
    print(
        f"computer's final cards: {computer_cards} and score: {computer_score}")
    print(compare(my_score, computer_score))


while input("Do you want to play a game? Type 'y' or 'n': ") == "y":
    game()
