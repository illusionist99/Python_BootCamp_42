class Recipe:
    """Recipe class"""
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        if name == "":
            raise ValueError
        self.name = name
        if (not str(cooking_lvl).isdigit()) or (cooking_lvl < 1 or cooking_lvl > 5):
            raise ValueError
        self.cooking_lvl = cooking_lvl
        if not str(cooking_time).isdigit() or cooking_time < 0:
            raise ValueError
        self.cooking_time = cooking_time
        if not str(cooking_time).isdigit():
            raise ValueError
        self.cooking_time = cooking_time
        if not ingredients:
            raise ValueError
        self.ingredients = ingredients
        self.description = description
        if recipe_type != "lunch" and recipe_type != "desert" and recipe_type != "starter":
            raise ValueError
        self.recipe_type = recipe_type

    def __str__(self):
        """Return The string to print with recipe info"""
        return '{} Ingredients are {} It Takes {} minutes To be Prepared for {}.' \
               '\nRecipe Description : {}'.format(self.name, ", ".join(map(str, self.ingredients)), self.cooking_time, self.recipe_type,self.description)
