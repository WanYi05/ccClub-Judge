n = int(input())
all_data = input().split() #武藏 2 小次郎 1 喵喵 2

food_dict = {}

if len(all_data) == n * 2:
    for i in range(0, len(all_data), 2):
        name = all_data[i]
        try:
            count = int(all_data[i+1])
            food_dict[name] = count
        except ValueError:
            print(f"數量 '{all_data[i+1]}' 不是有效的數字。")
            food_dict = {} # 清空字典，因為有錯誤
            break
else:
    print("輸入的資料數量與指定的字典數量不符。")

print(food_dict)