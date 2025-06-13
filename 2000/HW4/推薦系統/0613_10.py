users = {}
order = []

while True:
    line = input("請輸入顧客購買紀錄(或輸入end結束):")
    if line == "end":
        break

    parts = line.split()
    name = parts[0]
    items = parts[1:]

    print(f"讀取顧客:{name}，購買商品:{items}，購買商品:{items}")

    users[name] = items
    

    """
    line = "凱文 錢包 鑰匙 卡片 番茄"
    # name = "凱文"
    # items = ["錢包", "鑰匙", "卡片", "番茄"]

    users[name] = items
    # → users["凱文"] = ["錢包", "鑰匙", "卡片", "番茄"]

    users["凱文"]  # ➜ ["錢包", "鑰匙", "卡片", "番茄"]
    """

    order.append(name)
    """
    # 紀錄顧客輸入的順序
    Input :
    凱文 ...
    小明 ...
    小美 ...

    order = ["凱文", "小明", "小美"]
    """