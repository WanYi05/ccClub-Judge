lines = []

while True:
    line = input()
    if line == "end":
        break  # 當輸入 'end' 時，跳出迴圈
    lines.append(line)


for l in lines:
    if ',' in l:
        # 如果輸入字串中已經包含逗號，則直接列印
        print(l)
    else:
        # 否則，嘗試將其轉換為整數並格式化為千分位
        try:
            num = int(l)
            formatted_num = format(num, ",")
            print(formatted_num)
        except ValueError:
            # 如果輸入的不是有效的整數（不含逗號），則提示錯誤
            print(f"'{l}' 不是有效的整數，無法轉換為千分位數。")