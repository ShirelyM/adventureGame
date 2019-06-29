import os
from person.Person import Person

## Main script
if __name__ == '__main__':
    curDir = os.getcwd()
    swampPath = os.path.join(curDir, 'gamedata', 'players', 'SwampDonkey.xml')
    joePath = os.path.join(curDir, 'gamedata', 'players', 'CaptainJoe.xml')
    mike = Person()
    mike.fromFile(swampPath)
    justin = Person()
    justin.fromFile(joePath)

    print None
