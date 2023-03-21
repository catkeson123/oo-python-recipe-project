from recipeingredient import *

class Recipe:

    all = []

    def __init__(self):
        self.users = []
        self.ingredients = []
        self.allergens = []

    def add_ingredients(self, ingredients)
        
        for i in ingredients:
            RecipeIngredient(i, self)

        self.ingredients = [recing.ingredient for recing in RecipeIngredient.all if recing.recipe == self]
        

#  Recipe#add_ingredients should take an list of ingredient instances as an argument, and associate each of those ingredients with this recipe





# Recipe.most_popular should return the recipe instance with the highest number of users (the recipe that has the most recipe cards)
# Recipe#allergens should return all of the Ingredients in this recipe that are allergens for Users in our system.
#