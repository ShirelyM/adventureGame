class Hair(object):
    ## Constructor.
    def __init__(self):
        self.reset()

    ## Set the hair color and hair length.
    # @param hairColor   Integer representing the person's hair color.
    # @param hairLength  Integer representing the person's hair length
    def setAll(self, hairColor, hairLength):
        self.setHairColor(hairColor)
        self.setHairLength(hairLength)

    ## Reset member variables.
    def reset(self):
        self.m_hairColor      = hairColor
        self.m_hairLength     = hairLength

    ## Retrieve the hair color.
    # @return   Integer representing person's hair color.
    def getHairColor(self):
        return self.m_hairColor

    ## Set the hair color.
    # @param hairColor   integer representing the person's hair color.
    def setHairColor(self, hairColor):
        if not isinstance(hairColor, int):
            raise TypeError("Expected hair color to be a integer")
        self.m_hairColor = hairColor

    ## Retrieve the hair length.
    # @return   integer representing person's hair length.
    def getHairLength(self):
        return self.m_hairLength

    ## Set the hair length.
    # @param hairLength   String representing the person's hair length.
    def setHairLength(self, HairLength):
        if not isinstance(hairLength, int):
            raise TypeError("Expected hair length to be a integer")
        self.m_hairLength = hairLength

