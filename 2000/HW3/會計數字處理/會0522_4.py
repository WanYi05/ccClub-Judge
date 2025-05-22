lines = []
total_sum = 0 # 初始化總和變數

# print("請輸入整數 (可含千分位逗號)，輸入 'end' 結束：")

while True:
    line = input()
    if line == "end":
        break  # 當輸入 'end' 時，跳出迴圈
    
    # 處理輸入，將其轉換為數字並加總
    try:
        if ',' in line:
            # 如果輸入字串中包含逗號，先移除逗號再轉換為整數
            numeric_value = int(line.replace(',', '')) 
        else:
            # 如果不含逗號，直接轉換為整數
            numeric_value = int(line)
        
        total_sum += numeric_value # 將轉換後的數值加到總和中
        lines.append(line) # 將原始輸入保留在 lines 列表中，以便之後顯示
        
    except ValueError:
        # 如果輸入的不是有效的整數，則跳過加總並發出警告
        print(f"警告：'{line}' 不是有效的整數，將跳過此值不予加總。")
        # 這裡不將無效輸入加入 lines 列表，避免後續列印
        
# 最後，將總和格式化為千分位數並列印
# 由於你確定輸入都是整數，所以 total_sum 也會是整數，直接格式化即可
formatted_total_sum = format(int(total_sum), ",") 

print(formatted_total_sum)