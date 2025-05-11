# a = input()

# vowel = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

# seen = set()

# v_count = 0

# for i in a:
#     if i in vowel and i not in seen:
#         seen.add(i)
#         v_count = v_count+1

# print(v_count)

# =============================================


# result = ""

# while True: 
#     line = input() 

#     if not line:  
#         break
#     result = result+1

# print(sorted(result))

# 先把每一行存到 list 中，再排序，最後再組合成字串。




# ============



# lines = []  # 用來儲存所有輸入的行

# while True:
#     line = input()
#     if not line:
#         break
#     lines.append(line)  # 儲存每行到 list 中

# lines.sort()  # 進行 a~z 排序
# result = "\n".join(lines)  # 用換行符號組成多行字串

# print(result)


# ==============

# 🔧 需求整理：
# 多行輸入，直到空行為止
# 每行輸入保留（幾行輸入就幾行輸出）
# 根據每行字串的「母音數量」排序（少的排前面）
# 輸出為多行字串

vowels = set('AEIOUaeiou')  # 用 set 查找效率更快
lines = []

while True:
    line = input()
    if not line:
        break
    lines.append(line)

# 排序依據：每行字串中的母音數量
def count_vowels(s):
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count

""" 
# 簡潔寫法:
# def count_vowels(s):
#     return sum(1 for ch in s if ch in vowels)
"""


lines.sort(key=count_vowels)  # 排序時以母音數量為 key

result = "\n".join(lines)  # 多行輸出
print(result)