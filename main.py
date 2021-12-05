import random
import os
import time
import numpy as np

WAIT = 0.5
NUMBER_OF_BALLS = 75


def generate_number() -> int:
    return random.randint(1, 75)


def clear_screen() -> None:
    if os.name in ("nt", "dos"):
        command = "cls"
    else:
        command = "clear"
    os.system(command)


def print_card(card, heading="") -> str:
    output = f"-- {heading.upper()} -- \n"

    return output + str(np.matrix(card))


def print_cards(cards: list) -> None:
    for i in range(len(cards)):
        print(print_card(cards[i], heading=f"Card {i + 1}"))
        print("\n\n\n")
    time.sleep(WAIT)


def transpose(card: list) -> list:
    tranposed_card = list(zip(*card))
    for i in range(len(tranposed_card)):
        tranposed_card[i] = list(tranposed_card[i])

    return tranposed_card


def generate_card() -> list:
    return [[random.randint(1, 75) for _ in range(5)] for _ in range(5)]


def mark_horizontal(card: list, number: int) -> list:
    for row in card:
        if number in row:
            row[row.index(number)] = "X"
    return card


def mark_vertical(card: list, number: int) -> list:
    tranposed_card = transpose(card)
    for row in tranposed_card:
        if number in row:
            row[row.index(number)] = "X"

    return transpose(tranposed_card)


def mark_card(card: list, number: int) -> list:
    return mark_horizontal(mark_vertical(card, number), number)


def check_horizontal(card: list) -> bool:
    for row in card:
        if set(row) == set("X"):
            return True
    return False


def check_vertical(card: list) -> bool:
    tranposed_card = transpose(card)

    for row in tranposed_card:
        if set(row) == set("X"):
            return True
    return False


def check_card(card: list) -> bool:
    return check_horizontal(card) or check_vertical(card)


def main():

    card_1 = generate_card()
    card_2 = generate_card()

    winner = False

    cards = [card_1, card_2]

    numbers = [generate_number() for _ in range(NUMBER_OF_BALLS)]
    i = 0

    print_cards(cards)

    time.sleep(WAIT)
    clear_screen()

    while i < NUMBER_OF_BALLS and (not check_card(card_1) or not check_card(card_2)):
        number = numbers[i]

        print(f"Calling for {number}")

        card_1 = mark_card(card_1, number)
        card_2 = mark_card(card_2, number)

        cards = [card_1, card_2]

        print_cards(cards)
        clear_screen()

        if check_card(card_1):
            print("Player 1 says BINGO")
            print(print_card(card_1, heading="Card 1"))
            winner = True
            break

        if check_card(card_2):
            print("Player 2 says BINGO")
            print(print_card(card_2, heading="Card 2"))
            winner = True
            break

        i += 1

    if not winner:
        print("No Winner This Time, ran out of balls")


if __name__ == '__main__':
    main()
