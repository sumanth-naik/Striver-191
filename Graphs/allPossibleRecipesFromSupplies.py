recipes = ["bread","sandwich","burger"]
ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
supplies = ["yeast","flour","meat"]

recipes = ["xevvq","izcad","p","we","bxgnm","vpio","i","hjvu","igi","anp","tokfq","z","kwdmb","g","qb","q","b","hthy"]
ingredients = [["wbjr"],["otr","fzr","g"],["fzr","wi","otr","xgp","wbjr","igi","b"],["fzr","xgp","wi","otr","tokfq","izcad","igi","xevvq","i","anp"],["wi","xgp","wbjr"],["wbjr","bxgnm","i","b","hjvu","izcad","igi","z","g"],["xgp","otr","wbjr"],["wbjr","otr"],["wbjr","otr","fzr","wi","xgp","hjvu","tokfq","z","kwdmb"],["xgp","wi","wbjr","bxgnm","izcad","p","xevvq"],["bxgnm"],["wi","fzr","otr","wbjr"],["wbjr","wi","fzr","xgp","otr","g","b","p"],["otr","fzr","xgp","wbjr"],["xgp","wbjr","q","vpio","tokfq","we"],["wbjr","wi","xgp","we"],["wbjr"],["wi"]]
supplies = ["wi","otr","wbjr","fzr","xgp"]



def topoSort(recipe, recipeIngredientsMap, cookableItems, visited):
    visited.add(recipe)
    if recipe not in recipeIngredientsMap:
        if recipe not in cookableItems:
            return False
        return True
    for ingredient in recipeIngredientsMap[recipe]:
        if not ingredient in cookableItems:
            if ingredient in visited: 
                return False
            if topoSort(ingredient, recipeIngredientsMap, cookableItems, visited):
                cookableItems.add(ingredient)
            else:
                return False
    return True



def findAllRecipes(recipes, ingredients, supplies):

    recipeSet = set(recipes)
    recipeIngredientsMap = {}
    for index, recipe in enumerate(recipes):
        recipeIngredientsMap[recipe] = []
        for ingredient in ingredients[index]:
            recipeIngredientsMap[recipe].append(ingredient)

    visited = set()
    cookableItems = set(supplies)
    for recipe in recipeSet:
        if recipe not in cookableItems:
            if topoSort(recipe, recipeIngredientsMap, cookableItems, visited):
                cookableItems.add(recipe)
    return list(cookableItems.intersection(recipeSet))

print(findAllRecipes(recipes,ingredients,supplies))