from person.Person import Person

## Represents a poker player.
class PokerPlayer(Person):
    #Constuctor
    def __init__(self):
         Person.__init__(self)
         self.m_pokerHand = None

    ## Retrieve the person's poker hand.
    # @return   hand object.
    def gethand(self):
        return self.m_pokerHand


    ## Set the person's poker hand.
    # @param pokerHand  hand object representing the person's pokerHand.
    def sethand(self, pokerHand):
         self.m_pokerHand = pokerHand



