# 讀取輸入字串
s = input().strip()  # 例如 "ABC" 或 "BED"

# 將字母組合轉換為數字 (A=1, B=2, ..., Z=26)
total = 0
for c in s:
    value = ord(c.upper()) - ord('A') + 1  # A=1, B=2, ..., Z=26
    total = total * 26 + value  # 按照26進位計算

# 根據數字計算最少的紙鈔和硬幣數量
denominations = [1000, 500, 100, 50, 10, 1]  # 可能的面額
payment = []

for denom in denominations:
    count = total // denom  # 計算該面額需要幾張
    payment.append(count)  # 儲存這個面額需要的數量
    total -= count * denom  # 更新剩餘金額

# 輸出結果，將數量以逗號分隔
print(','.join(map(str, payment)))