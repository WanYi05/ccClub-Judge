# 讀入背包最大承重
w = int(input())

# 讀入物品數量
n = int(input())

# 讀入每個物品的資訊：名稱、價值、重量
items = []
for _ in range(n):
    name, value, weight = input().split()
    value = int(value)
    weight = int(weight)
    cp = value / weight  # 計算 CP 值
    items.append({'name': name, 'value': value, 'weight': weight, 'cp': cp})

# 開始貪婪選擇
current_weight = 0
selected_items = []

while True:
    # 找出所有目前可以裝得下的物品
    candidates = [item for item in items if item['weight'] + current_weight <= w]

    if not candidates:
        break  # 沒東西可以選就結束

    # 按照 CP 值由大到小、重量由小到大排序
    candidates.sort(key=lambda x: (-x['cp'], x['weight']))

    # 選出第一個（CP值最高且最輕的）物品
    chosen = candidates[0]
    selected_items.append(chosen['name'])
    current_weight += chosen['weight']

    # 把這個物品從待選清單中移除
    items.remove(chosen)

    # 🧠 為了確保每一個物品只能選一次，避免重複放入背包。
    # 有可能會發生: 一直選到同一個「CP值最高且放得下」的物品，然後重複加入背包，
    # 導致：
    # 明明物品只能選一次，卻像「無限複製」那樣用不完。
    # 結果錯誤，演算法會選錯東西，甚至進入死循環（一直挑同一個物品）。

# 輸出每次選到的物品名稱
for name in selected_items:
    print(name)