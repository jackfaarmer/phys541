import random

class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __str__(self):
        return f"{self.color} {self.value}"


class Deck:
    def __init__(self):
        colors = ['Blue', 'Green', 'Red', 'Yellow']
        values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Skip', 'Reverse']

        self.cards = [Card(color, val) for color in colors for val in values]

    def shuffle_deck(self):
        random.shuffle(self.cards)
        print("cards shuffled")

    def reshuffle_deck(self, discarded):
        reshuffle_cards = discarded[:-1]
        random.shuffle(reshuffle_cards)
        self.cards.extend(reshuffle_cards)
        discarded.clear()
        discarded.append(reshuffle_cards.pop())

    def draw_card(self):
        card = self.cards.pop()
        return card

class Player:
    def __init__(self, player_name='I didn\'t give myself a name'):
        self.player_name = player_name
        self.cards = []

    def draw_cards(self, cards, num_cards=1):
        for i in range(num_cards):
            self.cards.append(cards.draw_card())

    def play(self, index, discarded):
        played = self.cards.pop(index)
        discarded.append(played)
        return played

    def get_valid_card(self, discarded):
        for card_index, card in enumerate(self.cards):
            if card.color ==  discarded[-1].color or card.value == discarded[-1].value:
                return card_index
        return None # return invalid card
