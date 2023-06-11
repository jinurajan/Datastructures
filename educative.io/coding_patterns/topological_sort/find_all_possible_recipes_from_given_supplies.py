"""
A list of recipes a chef can prepare from the supplied items is given. Ingredients required to prepare a recipe are mentioned in the ingredients list. The ith recipe has the name 
recipes 
i, and you can create it if you have all the needed ingredients from the ingredients i list. A recipe may be listed as an ingredient in a different recipe. For example, the input may specify that custard is an ingredient in a trifle recipe or that trifle is an ingredient in a custard recipe.

Identify which recipes a chef can prepare from the given ingredients from the supplies list.

"""


from collections import defaultdict


def find_recipes(recipes, ingredients, supplies):
    adj_list = defaultdict(list)
    indegrees = {recipe: 0 for recipe in recipes}

    n = len(ingredients)
    for recipe, ingredient_list in zip(recipes, ingredients):
        for ingredient in ingredient_list:
            adj_list[ingredient].append(recipe)
            indegrees[recipe] += 1
    
    result = []
    while supplies:
        ingredient = supplies.pop(0)
        for l in adj_list[ingredient]:
            indegrees[l] -= 1
            if indegrees[l] == 0:
                supplies.append(l)
                result.append(l)
    return result