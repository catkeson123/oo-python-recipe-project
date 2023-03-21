class Ingredient:
    all = []
    
    def __init__(self, name):
        self.name=name
        Ingredient.all.append(self)

    def most_common_allergen(self):
        pass
