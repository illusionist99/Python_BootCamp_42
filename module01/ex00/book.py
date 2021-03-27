import datetime
from recipe import Recipe

class Book:
    name = ""
    last_update = 0
    creation_date = 0
    recipe_list = {
        "lunch": {},
        "starter": {},
        "dessert": {},
    }

    def __init__(self, name):
        self.name = name
        self.creation_date = datetime.datetime.now()

    def get_recipe_by_name(self, recipe_name):
        """Print a recipe with the name `name` and return the instance"""
        for key, value in self.recipe_list.items():
            for name, recipe_value in value.items():
                if name == recipe_name:
                    print(name, recipe_value)
                    return recipe_value

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        lst = self.recipe_list[recipe_type]
        return ", ".join(map(str, lst.keys()))

    def add_recipe(self, recipe):
        if not isinstance(recipe, Recipe):
            raise ValueError
        """Add a recipe to the book and update last_update"""
        if (recipe.recipe_type == "lunch") or (recipe.recipe_type == "starter") or (recipe.recipe_type == "dessert"):
            self.recipe_list[recipe.recipe_type].update({recipe.name : recipe})
            self.last_update = datetime.datetime.now()
        else:
            raise ValueError
        return



