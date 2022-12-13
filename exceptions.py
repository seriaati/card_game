class NotThirtyCard(Exception):
    def __init__(self):
        self.message = "Deck must have 30 cards"