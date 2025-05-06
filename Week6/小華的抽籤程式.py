import random

# 讀入輸入資料
r0, count = map(int, input().split())

# 初始化亂數種子
random.seed(r0)

# 生成 a, b, c
a = random.randint(1, 1_000_000_000)
b = random.randint(1, 1_000_000_000)
c = random.randint(1, 10_000)

# 計算並輸出 ri 值
ri = r0
for _ in range(count):
    ri = (a * ri + b) % c
    print(ri)
