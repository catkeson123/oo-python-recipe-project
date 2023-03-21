class Allergy:
    all = []

    def __init__(self, ingredient, user):
        self.ingredient = ingredient
        self.user = user
        Allergy.all.append(self)