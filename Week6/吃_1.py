def find_coefficients(total, val1, val2, val3):
    # """
    # 找出三個符合遞減條件的係數，使它們分別乘以三個給定數值後的總和等於目標總和。

    # Args:
    #     total: 目標總和。
    #     val1: 第一個單項數值。
    #     val2: 第二個單項數值。
    #     val3: 第三個單項數值。

    # Returns:
    #     一個包含三個係數的元組 (coeff1, coeff2, coeff3)，如果找到符合條件的係數。
    #     如果找不到，則返回 None。
    # """
    for c1 in range(total // val1 + 1):
        for c2 in range(c1 + 1):
            for c3 in range(c2 + 1):
                if c1 * val1 + c2 * val2 + c3 * val3 == total and c1 > c2 > c3:
                    return (c1, c2, c3)
    return None

# 讓使用者輸入四個數字
try:

    total = int(input())
    val1 = int(input())
    val2 = int(input())
    val3 = int(input())

    # 尋找符合條件的係數 (沿用之前的函數)
    def find_coefficients(total, val1, val2, val3):
        for c1 in range(total // val1 + 1):
            for c2 in range(c1 + 1):
                for c3 in range(c2 + 1):
                    if c1 * val1 + c2 * val2 + c3 * val3 == total and c1 >= c2 >= c3:
                        return (c1, c2, c3)
        return None

    coefficients = find_coefficients(total, val1, val2, val3)

    if coefficients:
        print(coefficients[0], coefficients[1], coefficients[2])
        # print(f"驗算: {val1}*{coefficients[0]} + {val2}*{coefficients[1]} + {val3}*{coefficients[2]} = {total}")
    else:
        print("找不到符合條件的係數組合。")

except ValueError:
    print("輸入的不是有效的整數，請重新輸入！")