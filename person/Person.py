from person.Name import Name
from person.Hair import Hair
from person.Clothes import Clothes

import xml.etree.ElementTree as ET

## Represents a person's base characteristics.
class Person(object):
    ## Constructor.
    def __init__(self):
        self.reset()

    ## Reset all member variables
    def reset(self):
        self.m_name = Name()
        self.m_gender = None
        self.m_hair = Hair()
        self.m_eyeColor = None
        self.m_clothes = Clothes()

    ## Populate a person object from an XML file.
    # @param filePath   Path to the file that is to be used to populate the Person object.
    def fromFile(self, filePath):
        root = ET.parse(filePath)

    ## Retrieve the person's name.
    # @return   Name object.
    def getName(self):
        return self.m_name

    ## Set the person's name.
    # @param name   Name object.
    def setName(self, name):
        if not isinstance(name, Name):
            raise TypeError("Expected 'name' to be of type Name")
        self.m_name = name

    ## Retrieve the person's gender.
    # @return   Integer value corresponding to Gender constant.
    def getGender(self):
        return self.m_gender

    ## Set the person's gender.
    # @param gender   Gender constant.
    def setGender(self, gender):
        if not isinstance(gender, int):
            raise TypeError("Expected 'gender' to be of type int")
        self.m_gender = gender

    ## Retrieve the person's hair.
    # @return   Hair object.
    def getHair(self):
        return self.m_hair

    ## Set the person's hair.
    # @param hair   Hair object.
    def setHair(self, hair):
        if not isinstance(hair, Hair):
            raise TypeError("Expected 'hair' to be of type Hair")
        self.m_hair = hair

    ## Retrieve the person's eye color.
    # @return   Integer value corresponding to EyeColor constant.
    def getEyeColor(self):
        return self.m_eyeColor

    ## Set the person's eye color.
    # @param color   EyeColor constant.
    def setEyeColor(self, color):
        if not isinstance(color, int):
            raise TypeError("Expected 'color' to be of type int")
        self.m_eyeColor = color

    ## Retrieve the person's clothes.
    # @return   Clothes object.
    def getClothes(self):
        return self.m_clothes

    ## Set the person's clothes.
    # @param clothes   Clothes object.
    def setClothes(self, clothes):
        if not isinstance(clothes, Clothes):
            raise TypeError("Expected 'clothes' to be of type Clothes")
        self.m_clothes = clothes