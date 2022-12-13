class TooManyCharacters(Exception):
    def __init__(self):
        self.message = "A player can't have more than 3 characters"

class TooManyCards(Exception):
    def __init__(self):
        self.message = "A deck can't have more than 30 cards"