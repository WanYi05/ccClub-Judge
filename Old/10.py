def int_to_chinese(num):
    """
    將一百以內的阿拉伯數字轉換為中文數字字串。

    Args:
        num: 一百以內的整數。

    Returns:
        轉換後的中文數字字串。如果輸入超出範圍，則返回錯誤訊息。
    """
    if not isinstance(num, int) or num < 0 or num > 99:
        return "輸入數字超出範圍 (0-99)"

    unit_dict = {0: "零", 1: "一", 2: "二", 3: "三", 4: "四", 5: "五", 6: "六", 7: "七", 8: "八", 9: "九", 10: "十"}

    if num < 10:
        return unit_dict[num]
    elif num < 20:
        return "十" + unit_dict[num % 10] if num % 10 != 0 else "十"
    else:
        ten = unit_dict[num // 10] + "十"
        unit = unit_dict[num % 10] if num % 10 != 0 else ""
        return ten + unit

if __name__ == "__main__":
    while True:
        try:
            user_input = input("請輸入一個 0 到 99 的數字 (輸入 'q' 結束): ")
            if user_input.lower() == 'q':
                break
            number = int(user_input)
            chinese_number = int_to_chinese(number)
            print(f"{number} 轉換為 {chinese_number}")
        except ValueError:
            print("輸入格式錯誤，請輸入整數。")