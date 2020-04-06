import sys


class Feature:
    """
    Class containing the information regarding features of an item
    """
    characteristics = []
    specifications = []
    manufacturer_url = ""

    def __str__(self):
        try:
            return "\ncharacteristics=" + "|".join([str(x) for x in self.characteristics]) + \
                   "\nspecifications=" + "|".join([str(x) for x in self.specifications]) + \
                   "\nmanufacturer_url=" + self.manufacturer_url
        except:
            print("Unexpected error:", sys.exc_info()[0])
            return ""
3

class Specification:
    """
    Class containing the information regarding an individual specification of an item
    """
    name = ""
    specs = []

    def __str__(self):
        return "\n" + self.name + "=" + "|".join(self.specs)
