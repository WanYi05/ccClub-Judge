postcard = []

# 讀取每一行直到結束
while True:
    try:
        line = input()
        if line.strip() == "":
            break
        postcard.append(line.strip().split())
    except EOFError:
        break

# 判斷長 (h) 和寬 (w)
h = len(postcard)  # 行數
w = len(postcard[0]) if h > 0 else 0  # 每行的元素數量

# 搜尋 "小明" 的位置
for i in range(h):
    for j in range(w):
        if postcard[i][j] == "小明":
            print(f"({i}, {j})")
            exit()
