# 計算串列中每個數字出現的次數
def count_numbers(nums):  # 定義一個函式叫 count_numbers，參數是 nums，代表輸入的一串數字（串列）。

    counts = {} 
    # 建立一個空字典 counts，用來存放數字出現的次數。
    # 字典的 key 是數字，value 是該數字出現的次數。
    
    for num in nums: # 使用迴圈，一個一個取出串列裡的數字 num。

        if num in counts: # 判斷字典 counts 中有沒有這個數字 num 的鍵。
            counts[num] += 1
        # 如果字典裡已經有這個數字，代表之前出現過了，就把該數字的計數器加一。
        
        else:
            counts[num] = 1
        # 如果字典裡沒有這個數字，表示第一次遇到，給這個數字的計數器設成 1。
        
    return counts

n = int(input("請輸入行數: "))
all_nums = []

for _ in range(n):
    line = list(map(int, input().split()))
    line.sort()            # 你如果需要，可以先排序每行
    print("排序後的數字:", line)
    all_nums.extend(line)  # 把這行的數字加到總串列

result = count_numbers(all_nums)

print("所有數字出現次數：")
for num, count in sorted(result.items()):
    print(f"數字 {num} 出現了 {count} 次")
