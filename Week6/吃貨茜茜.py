def find_coefficients_prioritize_price(sto_cap, foods):
    c = [food['capacity'] for food in foods]
    best_combo = None

    # 試探每種可能的食物數量組合
    for count1 in range(sto_cap // c[0] + 1):
        for count2 in range((sto_cap - count1 * c[0]) // c[1] + 1):
            for count3 in range((sto_cap - count1 * c[0] - count2 * c[1]) // c[2] + 1):
                total = count1 * c[0] + count2 * c[1] + count3 * c[2]
                if total == sto_cap:
                    counts = [count1, count2, count3]
                    if best_combo is None or counts > best_combo:
                        best_combo = counts

    # 返回最佳組合
    if best_combo:
        result = [0] * 3
        for i in range(3):
            result[foods[i]['original_index']] = best_combo[i]
        return result
    return None

try:
    # 輸入處理
    sto_cap = int(input())  # 胃容量
    P1 = int(input())  # 食物1價格
    C1 = int(input())  # 食物1容量
    P2 = int(input())  # 食物2價格
    C2 = int(input())  # 食物2容量
    P3 = int(input())  # 食物3價格
    C3 = int(input())  # 食物3容量

    # 使用輸入的資料創建食物字典
    food1 = {'price': P1, 'capacity': C1, 'original_index': 0}
    food2 = {'price': P2, 'capacity': C2, 'original_index': 1}
    food3 = {'price': P3, 'capacity': C3, 'original_index': 2}

    # 食物列表
    foods = [food1, food2, food3]
    
    # 根據價格從高到低排序
    foods_sorted = sorted(foods, key=lambda item: item['price'], reverse=True)

    # 找出最佳組合
    coefficients = find_coefficients_prioritize_price(sto_cap, foods_sorted)

    if coefficients:
        # 輸出各食物數量
        print(coefficients[0], coefficients[1], coefficients[2])

        # 計算原始順序對應的價格
        T1 = food1['price'] * coefficients[0]
        T2 = food2['price'] * coefficients[1]
        T3 = food3['price'] * coefficients[2]
        subtotal = T1 + T2 + T3

        # 計算總份數
        total_count = sum(coefficients)
        
        # 根據總份數決定額外的龍蝦與折扣
        bonus = 900 if total_count > 30 else 0
        discount = 450 * 0.8 if total_count > 20 else 450

        # 計算總花費
        total_price = subtotal + bonus - discount
        print(total_price)
    else:
        print("找不到符合條件的份數組合。")

except ValueError:
    print("輸入的不是有效的整數，請重新輸入！")
