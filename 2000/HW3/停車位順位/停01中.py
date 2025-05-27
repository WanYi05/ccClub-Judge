# A>B>C
# year 10>=5>=5
# 承上，若再相同，則依照門牌號碼：奇數 > 偶數


# 讀取第一行，取得住戶總數 n
# 這是告訴程式接下來會有多少筆住戶資料
n = int(input())

# 建立一個空列表來儲存所有住戶的資料
# 每筆住戶資料 (ID, 棟別, 年資, 門牌號碼) 會被儲存為這個列表中的一個子列表
residents_data = []

# 迴圈 n 次，每次讀取一行的住戶資料
# 這裡會重複執行 n 次，將每一行的資料讀入
for _ in range(n):
    # 讀取一行輸入（例如 "abc A 9 74"），並用空格分割成多個字串
    # input().split() 會將字串轉為列表，例如 ['abc', 'A', '9', '74']
    resident_info = input().split()
    
    # 將處理好的住戶資料（列表形式）加入到 residents_data 這個大列表中
    residents_data.append(resident_info)

# 定義棟別的優先級
# 我們使用一個字典來設定每棟的排序值：值越小，優先級越高，排序時會排在前面
# 例如，'A' 棟的優先級是 1，比 'B' 棟的 2 更高
building_priority = {'A': 1, 'B': 2, 'C': 3}

# 使用 sorted() 函數對 residents_data 列表進行排序
# sorted() 會返回一個新的已排序的列表，而不會改變原始的 residents_data 列表
#
# key 參數是一個 lambda 函數，它告訴 sorted() 如何決定每個元素的排序依據：
#   - lambda resident: resident 這裡代表 residents_data 中的每一個住戶資料子列表
#   - resident[1]: 這會取得住戶資料中的第二個元素，也就是「居住棟別」（例如 'A', 'B', 'C'）
#   - building_priority.get(resident[1], 99):
#       - .get() 是字典的方法，用來安全地取得鍵對應的值
#       - 如果 'resident[1]' (棟別) 在 building_priority 字典中找到，就返回其對應的數字（例如 'A' 返回 1）
sorted_residents = sorted(residents_data, key=lambda resident: building_priority[resident[1]])

# 承上，若棟別相同，則依照居住年資：10年以上(含) > 5年以上(含)，未滿10年 > 未滿5年


# 按照排序後的結果印出住戶ID
# 遍歷排序後的 sorted_residents 列表，一個接一個地處理每個住戶資料
for resident in sorted_residents:
    # resident[0] 是住戶資料列表中的第一個元素，也就是「住戶ID」
    print(f"住戶ID: {resident[0]}")