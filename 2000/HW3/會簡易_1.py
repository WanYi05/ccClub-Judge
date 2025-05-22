lines = []
total_sum = 0 # 初始化總和變數

# print("請輸入整數 (可含千分位逗號)，輸入 'end' 結束：")
# print("注意：此程式碼假設您只輸入有效數字，否則會報錯！") # 強調風險！

while True:
    line = input()
    if line == "end":
        break  # 當輸入 'end' 時，跳出迴圈
    
    # 處理輸入，將其轉換為數字並加總
    # 這裡沒有 try-except，如果輸入無效會直接報錯
    if ',' in line:
        # 如果輸入字串中包含逗號，先移除逗號再轉換為整數
        numeric_value = int(line.replace(',', '')) 
    else:
        # 如果不含逗號，直接轉換為整數
        numeric_value = int(line)
    
    total_sum += numeric_value # 將轉換後的數值加到總和中
    lines.append(line) # 將原始輸入保留在 lines 列表中，以便之後顯示
        
# 最後，將總和格式化為千分位數並列印
total = format(int(total_sum), ",") 

print(total)