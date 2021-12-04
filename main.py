import random, pprint

def generate_card() -> list:
    return [[random.randint(1, 75) for _ in range(5)] for _ in range(5) ]

def check_horizontal(card: list, number: int) -> list:
    for row in card:
        if number in row:
            row[row.index(number)] = "X"
    return card

def check_vertical(card: list, number: int) -> list:
    tranposed_card = list(zip(*card))
    for row in tranposed_card:
        if number in row:
            row[row.index(number)] = "X"

    return list(zip(*card))


def main():
    card = generate_card()
    

if __name__ == '__main__':
    main()