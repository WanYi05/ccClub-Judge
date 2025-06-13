n = int(input())
users = {}
order = []

# 讀取每個使用者的購買紀錄
while True:
    
    line = input()
    
    if line == "end":
        break

    parts = line.split()
    name = parts[0]
    items = parts [1:]
    users[name] = items
    order.append(name)

# 推薦系統主流程
for user in order:
    user_set = set(users[user])  # 使用者的購買商品set
    """
    users["凱文"] = ["錢包", "鑰匙", "卡片", "番茄"]
    user_set = set(users["凱文"])
    # ➜ user_set = {"錢包", "鑰匙", "卡片", "番茄"}
    """

    recommend_set = set()        # 用來避免重複推薦
    """
    🔸 意思是：
    建立一個空的集合，用來記錄已經推薦過的商品，避免重複。

    🔸 為什麼要它？
    如果同一商品被多位相似顧客推薦，我們要只推薦一次，這樣才不會重複出現在輸出中。
    """

    recommend_list = []          # 保留順序的推薦商品清單
    """
    🔸 意思是：
    建立一個空的列表，用來儲存推薦商品的順序清單

    🔸 為什麼還要 list？
    因為： set 沒有順序，不能保證推薦商品的順序正確
    我們要依照商品出現在資料中的順序來輸出（題目要求）

    """

    for other in order:
        if user == other:
            continue

        other_set =set(users[other])
        intersection = user_set & other_set
        similarity = len(intersection) / len(user_set)

        if similarity * 100 >= n:
            diff = other_set - user_set
            # 照商品順序推薦 (不是 set 順序)
            
            for item in users[other]:
                if item in diff and item not in recommend_set:
                    recommend_set.add(item)
                    recommend_list.append(item)
    
    # if recommend_list:
    #     print(user, *recommend_list)

    print(user, *recommend_list)