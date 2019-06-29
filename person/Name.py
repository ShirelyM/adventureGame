class Name(object):
    ## Constructor.
    # @param firstName  String representing the person's first name.
    # @param lastName   String representing the person's last name.
    def __init__(self, firstName = "John", lastName = "Doe"):
        self.reset()
        self.setAll(firstName, lastName)

    ## Reset member variables.
    def reset(self):
        self.m_firstName    = ""
        self.m_lastName     = ""

    ## Populate the name from an element tree node.
    # @param node   Element tree node to populate the name object from.
    def fromFile(self, node):
        self.setFirstName(node.find('first').text)
        self.setLastName(node.find('last').text)

    ## Retrieve the first name.
    # @return   String representing person's first name.
    def getFirstName(self):
        return self.m_firstName

    ## Set the first name.
    # @param name   String representing the person's first name.
    def setFirstName(self, name):
        if not isinstance(name, str):
            raise TypeError("Expected first name to be a string")
        self.m_firstName = name

    ## Retrieve the last name.
    # @return   String representing person's last name.
    def getLastName(self):
        return self.m_lastName

    ## Set the last name.
    # @param name   String representing the person's last name.
    def setLastName(self, name):
        if not isinstance(name, str):
            raise TypeError("Expected first name to be a string")
        self.m_lastName = name

    ## Set the first name and last name.
    # @param firstName  String representing the person's first name.
    # @param lastName   String representing the person's last name.
    def setAll(self, firstName, lastName):
        self.setFirstName(firstName)
        self.setLastName(lastName)