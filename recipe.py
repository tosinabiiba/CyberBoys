import random
# The list of ingredients in the fridge
fridge = ['eggs', 'milk', 'cheese', 'bread', 'butter']

# The recipe dictionary with ingredients as keys and the corresponding recipes as values
recipe_book = {
    'eggs': 'omelette',
    'milk': 'pancakes',
    'cheese': 'grilled cheese sandwich',
    'bread': 'toast',
    'butter': 'toast'
}

# The list of possible recipes
recipes = []

# Find all the recipes that can be made with the ingredients in the fridge
for ingredient in fridge:
    if ingredient in recipe_book:
        recipes.append(recipe_book[ingredient])

# Print the list of recipes
print(f'Recipes that can be made with the ingredients in the fridge: {recipes}')

# Choose a random recipe from the list
recipe = random.choice(recipes)

# Print the chosen recipe
print(f'Recipe chosen: {recipe}')
