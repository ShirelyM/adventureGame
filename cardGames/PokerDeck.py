import random

from copy import deepcopy
from cardGames.Card import Card

class PokerDeck(object):
    ## Constructor
    def __init__(self):
        self.reset()

    ## Reset the deck.
    def reset(self):
        self.m_cards = []
        for suit in range(0, 4):
            for value in range (1, 14):
                self.m_cards.append(Card(value, suit))

    ## Retrieve the list of cards in the deck
    # @return   List of Card objects
    def getCards(self):
        return self.m_cards

    ## Shuffle the deck
    def shuffle(self):
        random.shuffle(self.m_cards)

    ## Retrieve a single card from the top of the deck
    #@ return   Card object representing card on top of the deck
    def drawCard(self):
        if len(m_cards) > 0
            return m_cards.pop(0)
        print "The deck is empty"