class Feature:
    """
    Class containing the information regarding features of an item
    """
    characteristics = []
    specifications = []
    manufacturer_url= ""

    def __str__(self):
        return "\ncharacteristics="+self.characteristics+\
               "\nspecifications="+self.specifications+\
               "\nmanufacturer_url="+self.manufacturer_url

class Specification:
    """
    Class containing the information regarding an individual specification of an item
    """
    name = ""
    specs = []

    def __str__(self):
        return "\nname="+self.name+\
               "\nspec="+self.specs
