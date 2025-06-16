# 算CP值
w = int(input())      # 第一行輸入 w
n = int(input())      # 第二行輸入 n

data = []
for _ in range(n):    # 接下來輸入 n 行
    line = input()
    data.append(line)

# 測試印出資料
for i, d in enumerate(data, 1):
    print(f"第{i}行輸入：{d}")