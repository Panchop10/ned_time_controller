import random

from card import Card

if __name__ == '__main__':
    card = Card()

    print(card.id)

    #id = random.randint(1,9999)
    id = 6879
    print(id)

    card.save_id_number(id)
