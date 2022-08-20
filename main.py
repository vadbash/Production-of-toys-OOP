class Toy:
    def __init__(self, name, color, toy_type):
        self.name = name
        self.color = color
        self.toy_type = toy_type
    def creating_product(self):
        print(" {} Toy {} {} already done and ready to sell".format(self.color, self.toy_type, self.name))

class Disnay(Toy):
    def __init__(self, name, color, toy_type):
        Toy.__init__(self, name, color, toy_type)   
class SquarePants(Toy):
    def __init__(self, name, color, toy_type):
        Toy.__init__(self, name, color, toy_type)
class Smeshariki(Toy):
    def __init__(self, name, color, toy_type):
        Toy.__init__(self, name, color, toy_type)

def creating():
        print(" \n Purchase of raw materials process \n Tailoring process \n Dyeing process")
toys = [
    Disnay("Mickey mouse", "Black-red", "Disnay"),
    SquarePants("Spongebob", "Yellow", "Square Pants"),
    Smeshariki("Crosh", "Blue", "Smeshariki")
]

for toy in toys:
    creating()
    toy.creating_product()