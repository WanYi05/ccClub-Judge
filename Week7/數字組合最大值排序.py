# 使用者輸入一行數字
line = input()  # 例如：709 499 875

# 分割為多個字串
nums = line.split()  # ['709', '499', '875']

# 建立一個清單，存放 (重組後的最大值, 原始字串)
rearranged = []

for n in nums:
    max_n = ''.join(sorted(n, reverse=True))  # 把數字排列成最大
    rearranged.append((int(max_n), n))  # 存成元組，例如 (970, '709')

# 根據重組後的值排序（由小到大）
rearranged.sort()

# 取出排序後的原始字串（而不是最大值）

result = []
for item in rearranged:
    result.append(item[1])

# 簡潔寫法
# result = [item[1] for item in rearranged]

print(result)  # ['875', '709', '499']