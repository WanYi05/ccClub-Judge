# 讀取第一行，取得住戶總數 n
# 這是告訴程式接下來會有多少筆住戶資料
n = int(input())

# 建立一個空列表來儲存所有住戶的資料
# 每筆住戶資料 (ID, 棟別, 年資, 門牌號碼) 會被儲存為這個列表中的一個子列表
residents_data = []

# 迴圈 n 次，每次讀取一行的住戶資料
# 這裡會重複執行 n 次，將每一行的資料讀入
for i in range(n): # 使用 i 來記錄原始登記順序
    # 讀取一行輸入（例如 "abc A 9 74"），並用空格分割成多個字串
    resident_info = input().split()
    
    # 將原始的登記順序 (i) 加到住戶資料的末尾
    residents_data.append(resident_info + [i])

# 定義棟別的優先級
# 我們使用一個字典來設定每棟的排序值：值越小，優先級越高，排序時會排在前面
# 例如，'A' 棟的優先級是 1，比 'B' 棟的 2 更高
building_priority = {'A': 1, 'B': 2, 'C': 3}

# 定義居住年資的優先級
# 值越小，優先級越高
# 10年以上(含) > 5年以上(含)，未滿10年 > 未滿5年
def seniority_priority(years):
    years = int(years) # 將年資轉換為整數
    if years >= 10:
        return 1
    elif years >= 5:
        return 2
    else: # years < 5
        return 3

# 定義門牌號碼奇偶性的優先級
# 奇數 > 偶數
def address_priority(address):
    address = int(address) # 將門牌號碼轉換為整數
    if address % 2 != 0: # 奇數
        return 1
    else: # 偶數
        return 2

# 使用 sorted() 函數對 residents_data 進行多條件排序
# key 參數是一個 lambda 函數，它會根據多個條件返回一個 tuple
# sorted() 會依照 tuple 中元素的順序進行比較：
# 1. 棟別優先級 (值越小越優先)
# 2. 居住年資優先級 (值越小越優先)
# 3. 門牌號碼奇偶優先級 (值越小越優先)
# 4. 原始登記順序 (值越小越優先) - 這一項是為了處理所有條件都相同的情況
sorted_residents = sorted(residents_data, key=lambda resident: (
    building_priority[resident[1]],  # 棟別優先級 (直接從字典取得，假設 resident[1] 一定是 'A', 'B', 或 'C')
    seniority_priority(resident[2]),         # 居住年資優先級 (resident[2] 是年資)
    address_priority(resident[3]),           # 門牌號碼奇偶優先級 (resident[3] 是門牌號碼)
    resident[4]                               # 原始登記順序 (resident[4] 是原始索引，確保同級別的按登記順序排)
))

# 按照排序後的結果印出住戶ID
# 遍歷排序後的 sorted_residents 列表，一個接一個地處理每個住戶資料
for resident in sorted_residents:
    print(resident[0]) # resident[0] 是住戶ID