class Hair(object):
    ## Constructor.
    # @param hairColor   Integer representing the person's hair color.
    # @param hairLength  Integer representing the person's hair length
    def __init__(self, hairColor = 0, hairLength = 0.0):
        self.reset()
        self.setAll(hairColor, hairLength)

    ## Reset member variables.
    def reset(self):
        self.m_hairColor      = None
        self.m_hairLength     = None

    ## Populate a hair object from an elemtn tree node.
    # @param node   Element tree node containing the hair information.
    def fromFile(self, node):
        self.setHairColor(int(node.find('color').text))
        self.setHairLength(int(node.find('length').text))

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
    def setHairLength(self, hairLength):
        if not isinstance(hairLength, (int, float)):
            raise TypeError("Expected hair length to be a integer")
        self.m_hairLength = hairLength

    ## Set the hair color and hair length.
    # @param hairColor   Integer representing the person's hair color.
    # @param hairLength  Integer representing the person's hair length
    def setAll(self, hairColor, hairLength):
        self.setHairColor(hairColor)
        self.setHairLength(hairLength)