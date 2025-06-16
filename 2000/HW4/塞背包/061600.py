# 貪婪法舉例1

def greedy_coin_change(coins, amount):
    coins.sort(reverse=True)  # 先從最大面額開始找
    result = []
    
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    
    return result

# 範例：面額 [10, 5, 1] 湊出 28 元
print(greedy_coin_change([10, 5, 1], 28))
# ➜ [10, 10, 5, 1, 1, 1]

# ⚠️ 注意：這個方法在某些硬幣組合下可能無法找到最少的硬幣數，這是貪婪法的限制。

# 貪婪法舉例2
# 2️⃣ 活動選擇問題（Activity Selection)
# 目標：在不重疊的情況下選擇最多的活動。)

def activity_selection(activities):
    # activities: [(start, end), ...]
    activities.sort(key=lambda x: x[1])  # 依結束時間排序
    result = []
    end_time = 0
    
    for start, end in activities:
        if start >= end_time:
            result.append((start, end))
            end_time = end
    
    return result

# 範例：選出最多不重疊的活動
acts = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 9), (8, 9)]
print(activity_selection(acts))
# ➜ [(1, 3), (4, 6), (6, 7), (8, 9)]