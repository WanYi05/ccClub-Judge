# 讀取輸入：最高溫與最低溫
H, L = map(int, input().split())

# 計算平均氣溫
avg_temp = (H + L) / 2

# 讀取降雨機率，並檢查是否在有效範圍內
Rain = int(input())
if not (0 <= Rain <= 100):
    print("降雨機率不在有效範圍內")
    exit()

# 讀取紫外線指數（允許任意非負整數）
UV = int(input())
if UV < 0:
    print("紫外線指數不能為負數")
    exit()

# 判斷天氣狀況
if Rain <= 20:
    weather = "晴天"
elif Rain >= 70:
    weather = "雨天"
else:
    weather = "陰天"

# 判斷紫外線等級（可用於擴充需求）
if 0 <= UV <= 2:
    UV_level = "低量級"
elif 3 <= UV <= 5:
    UV_level = "中量級"
elif 6 <= UV <= 7:
    UV_level = "高量級"
elif 8 <= UV <= 10:
    UV_level = "過量級"
else:
    UV_level = "危險級"

# 判斷攜帶物品
accessories = []

# 規則1 & 規則2：雨天或紫外線高量級以上都要帶雨傘
if weather == "雨天" or UV >= 6:
    accessories.append("雨傘")

# 規則3：帽子（優先毛帽，其次棒球帽）
if avg_temp <= 18:
    accessories.append("毛帽")
elif weather == "陰天" and L <= 20:
    accessories.append("棒球帽")

# 規則4：紫外線中量級以上且為晴天時攜帶太陽眼鏡
if UV >= 3 and weather == "晴天":
    accessories.append("太陽眼鏡")

# 輸出結果
if accessories:
    print(" ".join(accessories))
else:
    print("空手出門")