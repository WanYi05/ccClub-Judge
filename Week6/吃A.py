# Input
sto_cap = int(input())

price1 = int(input())
cap1 = int(input())

price2 = int(input())
cap2 = int(input())

price3 = int(input())
cap3 = int(input())

# 建立食物清單，包含價值、容量與原始編號
foods = [
    {"price": price1, "cap": cap1, "index": 0},
    {"price": price2, "cap": cap2, "index": 1},
    {"price": price3, "cap": cap3, "index": 2}
]

# 依據 價值/容量 比從高到低排序
foods.sort(key=lambda x: x["price"] / x["cap"], reverse=True)

# 初始化吃的份數
counts = [0, 0, 0]
remain = sto_cap

# 吃最多能吃的份數（從高價值食物開始）
for food in foods:
    count = remain // food["cap"]
    counts[food["index"]] = count
    remain %= food["cap"]

# 計算總價值
total_value = (
    counts[0] * price1 +
    counts[1] * price2 +
    counts[2] * price3
)

# 若總數達 30，額外加 900 價值的龍蝦
total_count = sum(counts)
if total_count >= 30:
    total_value += 900

# 計算成本（20份以上打八折）
cost = 450 * 0.8 if total_count >= 20 else 450

# 利潤為總價值減去餐費
profit = total_value - cost

# Output
print(f"{counts[0]} {counts[1]} {counts[2]}")
print(f"{profit:.1f}")
