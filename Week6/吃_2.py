def find_coefficients_prioritize_price(sto_cap, foods):
    # 依照價格高到低已排序，抓出容量
    c = [food['capacity'] for food in foods]

    best_combo = None

    for count1 in range(sto_cap // c[0] + 1):
        for count2 in range((sto_cap - count1 * c[0]) // c[1] + 1):
            for count3 in range((sto_cap - count1 * c[0] - count2 * c[1]) // c[2] + 1):
                total = count1 * c[0] + count2 * c[1] + count3 * c[2]
                if total == sto_cap:
                    counts = [count1, count2, count3]
                    # 如果還沒有 best 或者新的 counts 在貴的食物份數上比較多，就取代
                    if best_combo is None or counts > best_combo:
                        best_combo = counts

    if best_combo:
        result = [0] * 3
        for i in range(3):
            result[foods[i]['original_index']] = best_combo[i]
        return result
    return None

try:
    sto_cap = int(input("請輸入總容量："))
    food1 = {'price': int(input("食物1價格：")), 'capacity': int(input("食物1容量：")), 'original_index': 0}
    food2 = {'price': int(input("食物2價格：")), 'capacity': int(input("食物2容量：")), 'original_index': 1}
    food3 = {'price': int(input("食物3價格：")), 'capacity': int(input("食物3容量：")), 'original_index': 2}

    foods = [food1, food2, food3]
    foods_sorted = sorted(foods, key=lambda item: item['price'], reverse=True)  # 價格排序

    coefficients = find_coefficients_prioritize_price(sto_cap, foods_sorted)

    if coefficients:
        print(coefficients[0], coefficients[1], coefficients[2])
        # 驗算：根據輸出的份數對照原始容量
        cap_sum = (
            food1['capacity'] * coefficients[0] +
            food2['capacity'] * coefficients[1] +
            food3['capacity'] * coefficients[2]
        )
        print(f"驗算: {food1['capacity']}*{coefficients[0]} + {food2['capacity']}*{coefficients[1]} + {food3['capacity']}*{coefficients[2]} = {cap_sum}")
    else:
        print("找不到符合條件的份數組合。")

except ValueError:
    print("輸入的不是有效的整數，請重新輸入！")
