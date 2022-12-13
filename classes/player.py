from typing import Dict, List
from classes.card import ActionCard, CharacterCard
from classes.deck import Deck
from classes.dice import Dice
from enums import Element
from exceptions import TooManyCharacters


class Player(object):
    def __init__(
        self,
        deck: Deck,
        dices: List[Dice],
        characters: List[CharacterCard],
        hand: List[ActionCard],
    ):
        self.deck = deck
        self.dices = dices
        self.characters = characters
        self.hand = hand
        self.active_character = None

        if len(self.characters) > 3:
            raise TooManyCharacters

    def set_active_character(self, character: CharacterCard):
        self.active_character = character

    def draw_card(self):
        self.hand.append(self.deck.action_cards.pop())

    def draw_cards(self, number: int):
        for _ in range(number):
            self.draw_card()

    def use_card(self, card: ActionCard):
        self.hand.remove(card)

        # use elemental dices first, if they exist in the card cost
        if any(
            dice.element != Element.NONE and dice.element != Element.BLACK
            for dice in card.cost
        ):
            for dice in card.cost:
                if dice.element != Element.NONE and dice.element != Element.BLACK:
                    # if the user has any omni dice, they can use it to pay this elemental dice
                    if Dice(Element.OMNI) in self.dices:
                        self.dices.remove(Dice(Element.OMNI))
                    else:
                        self.dices.remove(dice)

        # black dices
        if any(dice.element == Element.BLACK for dice in card.cost):
            # organize player's dice by element
            dices_by_element: Dict[Element, List[Dice]] = {}
            for dice in self.dices:
                if dice.element in dices_by_element:
                    dices_by_element[dice.element].append(dice)
                else:
                    dices_by_element[dice.element] = [dice]

            for element, dices in dices_by_element.items():
                # use omni dices first
                if element == Element.OMNI and len(dices) >= len(card.cost):
                    for _ in range(len(card.cost)):
                        self.dices.remove(Dice(Element.OMNI))
                    break
                # use any other elemental dices
                elif len(dices) >= len(card.cost):
                    for _ in range(len(card.cost)):
                        self.dices.remove(Dice(element))
                    break

        # none dices
        if any(dice.element == Element.NONE for dice in card.cost):
            for _ in range(len(card.cost)):
                self.dices.remove(Dice(Element.NONE))

        # TODO: some cards cost energy when being used

    def check_card_usability(self, card: ActionCard):
        # there are only three types of card costs right now:
        # 1. cost with black dice
        # 2. cost with none dice
        # 3. cost with elemental dice
        # it is currently not possible to have two types of card costs in one card

        # check if the card cost is 0
        if len(card.cost) == 0:
            return True

        # check if the card cost has black element dice
        elif any(dice.element == Element.BLACK for dice in card.cost):
            # count the number of dices of each element in the player's dices
            dices_by_element: Dict[Element, int] = {}
            for dice in self.dices:
                if dice.element in dices_by_element:
                    dices_by_element[dice.element] += 1
                else:
                    dices_by_element[dice.element] = 1
            if len(card.cost) in dices_by_element.values():
                return True

        # check if the card cost has none element dice
        elif any(dice.element == Element.NONE for dice in card.cost):
            # if the player any enough dices, they can play the card
            if len(self.dices) >= len(card.cost):
                return True

        # the cost of the card has an element dice
        else:
            if card.cost in self.dices:
                return True

        return False
