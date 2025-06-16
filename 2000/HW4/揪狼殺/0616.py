def count_numbers(nums): 
    counts = {} 
    for num in nums: 
        if num in counts: 
            counts[num] += 1
        else:
            counts[num] = 1
    return counts

n = int(input())
all_nums = []

for i in range(n):
    line = list(map(int, input().split()))
    line.sort()          
    print(f"第{i+1}行排序後的數字:", line)  
    all_nums.extend(line)   

result = count_numbers(all_nums)

print("所有數字出現次數：")
for num, count in sorted(result.items(), key=lambda x: x[1], reverse=True):
    print(f"數字 {num} 出現了 {count} 次")

# 建立 24 小時的人數統計
available = [0] * 24
for hour in all_nums:
    available[hour] += 1

# 找出所有人數 ≥12 的時間點
threshold = 12
qualified = [i for i, count in enumerate(available) if count >= threshold]

if not qualified:
    # 沒有任何時間滿12人，找出最多人數的時間（若有多個，取最小時間）
    max_count = max(available)
    best_time = [i for i, count in enumerate(available) if count == max_count][0]
    print("恬要約的時間：", best_time)
else:
    # 找連續段中最長的，並輸出起始時間
    longest = 1
    current_len = 1
    start = qualified[0]
    best_start = start

    for i in range(1, len(qualified)):
        if qualified[i] == qualified[i-1] + 1:
            current_len += 1
        else:
            if current_len > longest:
                longest = current_len
                best_start = qualified[i - current_len]
            current_len = 1

    # 最後再檢查一次（因為可能是尾巴才是最長）
    if current_len > longest:
        best_start = qualified[-current_len]

    print("恬要約的時間：", best_start)
