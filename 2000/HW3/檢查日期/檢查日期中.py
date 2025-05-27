all_number_lists = []

datedict = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

while True:
    line = input()

    if line == "end":
        break
    
    cleaned_line = line.replace(" ", "")
    num_list = [int(num) for num in cleaned_line.split(',')]
    
    # 檢查是否恰好有三個元素 (年、月、日)
    if len(num_list) != 3:
        print("error")
        continue # 跳過當前迴圈的其餘部分，處理下一個輸入

    year = num_list[0]
    month = num_list[1]
    day = num_list[2]


    # 1. 判斷年份是否合理
    if year > 0:
        # 2. 判斷月份是否合法 (1 到 12)
        if 1 <= month <= 12:
            # 獲取該月份的最大天數
            max_days_in_month = datedict[month]
            
            # 3. 判斷日期是否合法 (1 到該月份的最大天數)
            if 1 <= day <= max_days_in_month:
                print("OK")
                # 如果是合法的日期，可以選擇將其加入 all_number_lists
                all_number_lists.append(num_list) 
            else:
                print("error") # 日期不合法
        else:
            print("error") # 月份不合法
    else:
        print("error") # 年份不合法