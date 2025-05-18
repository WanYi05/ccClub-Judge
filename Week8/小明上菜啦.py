# 第一部分：食材庫存
n = int(input())
inventory_input = input().split()
inventory = {}
for i in range(0, len(inventory_input), 2):
    material = inventory_input[i]
    quantity = int(inventory_input[i+1])
    inventory[material] = quantity

# 第二部分：餐廳菜單
m = int(input())
menu = {}
for _ in range(m):
    menu_input = input().split()
    dish_name = menu_input[0]
    ingredients = {}
    for i in range(1, len(menu_input), 2):
        material = menu_input[i]
        quantity = int(menu_input[i+1])
        ingredients[material] = quantity
    menu[dish_name] = ingredients

# 第三部分：點餐單
k = int(input())
orders = [input() for _ in range(k)]

# 處理點餐
for order in orders:
    if order not in menu:
        print(False)  # 菜單上沒有這道料理
        continue

    required_ingredients = menu[order]
    can_cook = True

    # 檢查庫存是否足夠
    for material, required_quantity in required_ingredients.items():
        if material not in inventory or inventory[material] < required_quantity:
            can_cook = False
            break

    print(can_cook)

    # 如果可以製作，則更新庫存
    if can_cook:
        for material, required_quantity in required_ingredients.items():
            inventory[material] -= required_quantity