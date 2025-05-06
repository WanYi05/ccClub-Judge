def f(x):
    # 定義f(1) = 1
    if x == 1:
        return 1  # f(1) = 1
    
    if x % 2 != 0:  # 判斷是否為奇數
        # 當 x = 2k + 1 (k >= 1)，即大於 1 的正奇數，f(2k + 1) = f(k) + f(k + 1)。
        k = (x - 1) // 2  # k = (x - 1) // 2 = 求k
        return f(k) + f(k + 1)  # 使用遞迴公式 f(2k + 1) = f(k) + f(k + 1)
    
    # 當 x 是偶數時，我們要檢查是否可以表示為 2的n次方 * k 的形式
    # 當 x = 2^n * k (n >= 1, k >= 1)，即正偶數，f(2^n * k) = f(k)。

    # n = 0
    while x % 2 == 0:  # 檢查 x 是否是 2 的倍數
        x = x // 2 # 5>2>1 
        # n = n + 1 # >2 
    # k = n 
    # return k 
    # n > 2n *　ｋ　

    # 當 x 最終為奇數（x = k），返回 f(k)
    return f(x)


# 讓使用者輸入數字
num = int(input())

# 計算並顯示結果
print(f(num))  # 顯示 f(num) 的結果


