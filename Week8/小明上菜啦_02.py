num_recipes = int(input())

# 2
# 火箭隊 武藏 1 小次郎 1 喵喵 1
# 小智一行人 小智 1 小霞 1 小剛 1

recipes = []

for _ in range(num_recipes):
    line = input().split()
    if not line:
        print("警告：輸入行為空！")
        continue

    recipe_name = line[0]
    ingredients = {}
    if len(line) > 1:
        for i in range(1, len(line), 2):
            if i + 1 < len(line):
                ingredient_name = line[i]
                try:
                    quantity = int(line[i+1])
                    ingredients[ingredient_name] = quantity
                except ValueError:
                    print(f"警告：數量 '{line[i+1]}' 不是有效的數字，已忽略。")
            else:
                print(f"警告：材料 '{line[i]}' 後缺少數量，已忽略。")

    recipes.append({'料理名稱': recipe_name, '材料': ingredients})

# for recipe in recipes:
#     print("料理名稱:", recipe['料理名稱'])
#     print("材料:", recipe['材料'])