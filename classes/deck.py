from typing import List

from classes.card import ActionCard, CharacterCard
from exceptions import TooManyCards, TooManyCharacters


class Deck(object):
    def __init__(
        self, character_cards: List[CharacterCard], action_cards: List[ActionCard]
    ):
        self.cards: List[ActionCard | CharacterCard] = character_cards + action_cards
        self.character_cards = character_cards
        self.action_cards = action_cards
        if len(self.cards) != 30:
            raise TooManyCards
        if len(self.character_cards) != 3:
            raise TooManyCharacters
