import os
from person.Person import Person
from cardGames.PokerDeck import PokerDeck as deck

## Main script
if __name__ == '__main__':
    curDir = os.getcwd()
    swampPath = os.path.join(curDir, 'gamedata', 'players', 'SwampDonkey.xml')
    joePath = os.path.join(curDir, 'gamedata', 'players', 'CaptainJoe.xml')
    mike = Person()
    mike.fromFile(swampPath)
    justin = Person()
    justin.fromFile(joePath)

    newDeck = deck()
    for card in newDeck.getCards():
        print card

    print('\n\n\n\n')
    newDeck.shuffle()
    for card in newDeck.getCards():
        print card