lines = [] # 儲存每一行輸入的列表
total_sum = 0 # 累計數字總和

print("請輸入數字，輸入 'end' 結束：")
print("--- 觀察 'lines' 列表的變化 ---")

while True:
    line = input()
    if line == "end":
        break # 輸入 'end' 結束迴圈

    # 處理數字轉換和加總 (為簡潔，此處省略錯誤處理)
    # 實際應用中建議加入 try-except
    if ',' in line:
        numeric_value = int(line.replace(',', ''))
    else:
        numeric_value = int(line)
    
    total_sum += numeric_value

    # --- 關鍵部分：每次 'append' 後立即印出 'lines' ---
    print(f"\n--- 你剛剛輸入了: '{line}' ---")
    lines.append(line) # 將當前輸入的 'line' 加入到 'lines' 列表中

    print(f"目前 'lines' 列表的內容是: {lines}")
    print("---------------------------------")
    # --- 結束關鍵部分 ---

print("\n--- 所有輸入結束 ---")
print(f"最終 'lines' 列表儲存了所有輸入: {lines}")

# 計算並印出總和 (與 'lines' 列表無直接關係，只是為了完整性)
final_total = format(int(total_sum), ",")
print(f"所有數字的總和是: {final_total}")