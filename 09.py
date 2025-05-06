time_input = input("請輸入時間（格式 HH:MM）：")  # 例如輸入 16:52
add_min = int(input("請輸入要增加的分鐘數："))    # 例如輸入 35

# 分割字串取得時與分
hour_str, min_str = time_input.split(":")
hour = int(hour_str)
minute = int(min_str)

# 加上分鐘
minute += add_min

# 處理進位
hour += minute // 60
minute = minute % 60
hour = hour % 24  # 24 小時制
# 不能使用12小時制，會顯示錯誤時間

# 輸出，不補 0
print("新的時間是：", hour, ":", minute, sep="")
