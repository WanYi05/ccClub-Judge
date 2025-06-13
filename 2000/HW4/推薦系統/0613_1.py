# 讀取每個使用者的購買紀錄

users = {}
order = []

while True:
    line = input("請輸入顧客購買紀錄（或輸入 end 結束）：")  # 增加提示
    if line == "end":
        break

    parts = line.split()  
    name = parts[0]
    items = parts[1:]

    print(f"讀取顧客：{name}，購買商品：{items}")

    users[name] = items
    order.append(name)

# 輸入結束後，顯示全部資料
print("\n所有顧客資料如下：")
for name in order:
    print(f"{name}：{users[name]}")
