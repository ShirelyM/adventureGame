class Clothes(object):
    ## Constructor
    def __init__(self):
        self.reset()

    ## Reset the member variables
    def reset(self):
        self.m_top = None
        self.m_bottom = None
        self.m_shoes = None
        self.m_hat   = None

    ## Get the Top
    # @return   String representing the Top
    def getTop(self):
        return self.m_top

    ## Set the Top
    # @param top    String representing the top
    def setTop(self, top):
        if not isinstance(top, str):
            raise TypeError("Top expected a string")
        self.m_top = top

    ## Get the Bottom
    # @return   String representing bottoms
    def getBottom(self):
        return self.m_bottom

    ## Set the Bottom
    # @param bottom     String representing the bottoms
    def setBottom(self):
        if not isinstance(bottom, str):
            raise TypeError("Bottom expected a string")
        self.m_bottom = bottom

    ## Get the shoes
    # @return   String representing shoes
    def getShoes(self):
        return self.m_shoes

    ## Set the shoes
    # @param shoes  String representing the shoes.
    def setShoes(self):
        if not isinstance(shoes, str):
            raise TypeError("Shoes expected a string")
        self.m_shoes = shoes

    ## Get the hat
    # @return   String represent hat
    def getHat(self):
        return self.m_hat

    ## Set the hat
    # @param hat    String representing the hat
    def setHat(self):
        if not isinstance(hat, str):
            raise TypeERror("Hat expected a string")
        self.m_hat = hat