from typing import List

from classes.main_cards import Card
from exceptions import NotThirtyCard


class Deck(object):
    def __init__(self, cards: List[Card]):
        self.cards = cards
        if len(cards) != 30:
            raise NotThirtyCard