from collections import defaultdict
class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        suppliesSet = set(supplies)  # 将提供的供应品列表转换为集合，便于后续快速检查某个原料是否可用。
        recipesMap = {recipes[i]: ingredients[i] for i in range(len(recipes))}  # 创建一个映射，将每个食谱映射到它的原料列表。
        ans = []  # 初始化一个空列表，用于存储可以制作的食谱。

        for recipe in recipesMap:  # 遍历每个食谱。
            if self.canMake(recipe, suppliesSet, recipesMap, set()):  # 检查是否可以制作当前食谱。
                ans.append(recipe)  # 如果可以制作，将其添加到答案列表中。

        return ans  # 返回可以制作的食谱列表。

    def canMake(self, target, suppliesSet, recipesMap, seen):
        if target in suppliesSet:  # 如果目标食谱的原料直接在供应品中，返回 True。
            return True
        if target in seen:  # 如果目标食谱已经被检查过（防止循环依赖），返回 False。
            return False
        if target not in recipesMap:  # 如果目标食谱不在食谱映射中，表示我们不知道如何制作它，返回 False。
            return False
        seen.add(target)  # 将当前食谱添加到已检查的集合中。

        for ingredient in recipesMap[target]:  # 遍历目标食谱所需的每个原料。
            if not self.canMake(ingredient, suppliesSet, recipesMap, seen):  # 递归检查是否可以制作每个原料。
                return False  # 如果有任何一个原料不能制作，返回 False。

        suppliesSet.add(target)  # 将目标食谱添加到供应品集合中，表示现在可以制作它。
        return True  # 所有原料都可以制作，因此返回 True。


recipes = ["bread","sandwich","burger"]
ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
supplies = ["yeast","flour","meat"]

sol = Solution()
print(sol.findAllRecipes(recipes, ingredients, supplies))