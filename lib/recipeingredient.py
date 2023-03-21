class RecipeIngredient:
    all = []
    
    def __init__(self, ingredient, recipe):
        self.ingredient = ingredient
        self.recipe = recipe
        RecipeIngredient.all.append(self)


