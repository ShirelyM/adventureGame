class FiveCardHand(object):
    ## Constructor
    def __init__(self):
        self.reset()

    def reset(self):
        self.m_hand = {1:None, 2:None, 3:None, 4:None, 5:None}

    ## Add a card to the hand
    # @param card   The card object to be added to the hand
    def addCard(self, card):
        for key, value in self.m_hand.iteritems():
            if value is None:
                self.m_hand[key] = card
                return

        raise RuntimeError("The player's hand is already full")

    ## Switch the positions of two cards in the hand
    # @param pos1   Integer representing the position of the first card to be switched
    # @param pos2   Integer representing the position of the second card to be switched
    def switchCardPositions(self, pos1, pos2):
        cardCopy = deepcopy(self.m_hand[pos1])
        self.m_hand[pos1] = deepcopy(self.m_hand[pos2])
        self.m_hands[pos2] = cardCopy
