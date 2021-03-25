import time

cookbook = {
    "sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": "10",
    },
    "cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": "60",
    },
    "salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": "15",
    },
}


# Print Keys Only
def print_all_names():
    for key in cookbook.keys():
        print(key)


# Print Keys Only
#    for key in cookbook.keys():
#        print(key)
# Print Values Only
# for value in cookbook.values():
#    print(value)
# Print All Items
# for item in cookbook.items():
#    print(item)


def print_recipe(name):
    if not (name in cookbook):
        return
    recipe = cookbook[name]
    print("Ingredients list: {list}".format(list=recipe["ingredients"]))
    print("To be eaten for {type}.".format(type=recipe["meal"]))
    print("Takes {minutes} minutes of cooking.".format(minutes=recipe["prep_time"]))


def delete_recipe(name):
    del cookbook[name]


def add_recipe(name, ingredients, meal, prep_time):
    new_recipe = {
        name: {
            "ingredients": list(ingredients),
            "meal": meal,
            "prep_time": prep_time,
        },
    }
    cookbook.update(new_recipe)


def options(num):
    name = ""
    ingredients = []
    meal = ""
    prep_time = ""
    if num == 5:
        print("Quit !")
        exit(0)
    elif num == 4:
        print_all_names()
    elif num == 3:
        print_recipe(input("Please enter the recipe's name to get its details: "))
    elif num == 2:
        delete_recipe(input("Please enter the recipe's name to delete it: "))
    elif num == 1:
        name = input("Please enter the recipe's name: ")
        print("Please enter the recipe's ingredients: ")
        while True:
            try:
                ingredients.append(input(" -> "))
            except EOFError:
                break
        meal = input("Please enter the recipe's meal type: ")
        prep_time = input("Please enter the recipe's preparation time: ")
        add_recipe(name, ingredients, meal, prep_time)
    else:
        return -1
    return 0


def cookbook_prompt():
    num = 0
    name = ""
    ingredients = []
    meal = ""
    prep_time = ""
    while True:
        print("Please select an option by typing the corresponding number: ")
        print("1: Add a recipe")
        print("2: Delete a recipe")
        print("3: Print a recipe")
        print("4: Print the cookbook")
        print("5: Quit")
        print("CookBook $ ", end='')
        try:
            try:
                num = int(input())
            except ValueError:
                num = 0
        except EOFError:
            break
        if options(num) == -1:
            print("This option does not exist, please type the corresponding number.")
            print("To exit, enter 5.")
            try:
                num = int(input(">> "))
            except ValueError:
                num = 0
            if num == 5:
                print("Quit !")
                exit(0)
#        time.sleep(1)


cookbook_prompt()
