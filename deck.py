from random import shuffle
from card import Card
import deck_generators



class Deck(list):
    def __init__(self, cards: list=[], generate: bool=True, shuffle_deck: bool=False) -> None:
        if cards == [] and generate:
            cards = deck_generators.standard_52()
        list.__init__(self, cards)
        if shuffle_deck:
            self.reshuffle()


    def reshuffle(self) -> None:
        shuffle(self)


    def pick_card(self) -> Card:
        return self.pop()


    def add_card(self, card: Card):
        self.append(card)


class Hand(Deck):
    def __init__(self, cards: list=[], *args, **kwargs):
        Deck.__init__(self, cards, *args, **kwargs)


    @property
    def value(self) -> type:
        value_min = 0
        value_max = 0
        for card in self:
            match card.value:
                case 1:
                    value_min += card.value
                    value_max += 11
                case 11, 12, 13:
                    value_min += 10
                    value_max += 10
                case _:
                    value_min += card.value
                    value_max += card.value
        return (value_min, value_max)


    @property
    def bet(self) -> type:
        return self.bet


    @property.setter
    def bet(self, bet):
        self.bet = bet