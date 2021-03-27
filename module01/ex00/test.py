from book import Book
from recipe import Recipe

# list of ingredients (don't try them might kill ya)
ingredient = ["ffff", "dafsfa"]

# creating an instance from my class Book
x = Book("mybook")

f = Recipe("dddd", 5, 20, ingredient, "healthy", "lunch")
t = Recipe("tttt", 5, 20, ingredient, "healthy", "lunch")

# adding a recipe
Book.add_recipe(x, f)
Book.add_recipe(x, t)

print(Book.recipe_list)

print(Book.get_recipes_by_types(x, "lunch"))
print(x)

g = Book.get_recipe_by_name(x, "dddd")
s = Recipe.__str__(g)
print(s)

