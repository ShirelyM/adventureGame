class Card(object):
    ## Constructor
    # @param value  Integer representing the cards value
    # @param suit   Integer representing the cards suit
    def __init__(self, value = None, suit = None):
        self.reset()
        self.setAll(value, suit)
        self.suitDict = {0:'Clubs', 1:'Diamonds', 2:'Hearts', 3:'Spades'}
        self.valueDict = {1: 'Ace', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:'Jack', 12:'Queen', 13:'King'}

    ## Reset the cards attributes
    def reset(self):
        self.m_value = None
        self.m_suit = None

    ## Retrieve the cards value
    # @return   Integer representing the cards value.
    def getValue(self):
        return self.m_value

    ## Set the cards value.
    # @param value  Integer representing the cards value
    def setValue(self, value):
        if not isinstance(value, int):
            raise TypeError("Card value expected an integer")
        self.m_value = value

    ## Get the cards suit
    # @return   Integer representing the cards suit
    def getSuit(self):
        return self.m_suit

    ## Set the cards suit
    # @param suit   Integer representing the cards suit
    def setSuit(self, suit):
        if not isinstance(suit, int):
            raise TypeError("Card suit expected an integer")
        self.m_suit = suit

    ## Set all values for the card
    # @param value  Integer representing the cards value
    # @param suit   Integer representing the cards suit
    def setAll(self, value, suit):
        self.setValue(value)
        self.setSuit(suit)

    def __repr__(self):
        return (self.valueDict[self.getValue()] + ' of ' + self.suitDict[self.getSuit()])