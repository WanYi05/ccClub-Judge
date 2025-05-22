lines = []
total_sum = 0 # 初始化總和變數

# print("請輸入數字 (可含千分位逗號)，輸入 'end' 結束：")

while True:
    line = input()
    if line == "end":
        break  # 當輸入 'end' 時，跳出迴圈
    
    # 處理輸入，將其轉換為數字並加總
    try:
        if ',' in line:
            # 如果輸入字串中包含逗號，先移除逗號再轉換
            # 使用 float() 可以處理更大的數字範圍，即使是整數也沒問題
            numeric_value = float(line.replace(',', '')) 
        else:
            # 如果不含逗號，直接轉換為浮點數
            numeric_value = float(line)
        
        total_sum += numeric_value # 將轉換後的數值加到總和中
        lines.append(line) # 將原始輸入保留在 lines 列表中，以便之後顯示
        
    except ValueError:
        # 如果輸入的不是有效的數字，則跳過加總並發出警告
        print(f"警告：'{line}' 不是有效的數字，將跳過此值不予加總。")
        # 這裡不將無效輸入加入 lines 列表，避免後續列印
        

# print("\n---")
# print("您輸入的數值列表：")
# for l in lines:
    # 這裡只是單純列印輸入過的值，不做額外格式化
    # print(l) 
# print("---")

# 在迴圈結束後，對總和進行格式化並列印
# 判斷總和是否為精確的整數，以便決定格式化時是否帶小數點
if total_sum == int(total_sum):
    # 如果總和是整數，格式化為不帶小數點的千分位數
    formatted_total_sum = format(int(total_sum), ",") 
else:
    # 如果總和是浮點數，格式化為帶小數點的千分位數
    formatted_total_sum = format(total_sum, ",") 

# print(f"\n所有數字的總和是：{formatted_total_sum}")
print(formatted_total_sum)
