# with open('04_3.txt', 'r', encoding='utf-8') as f:
#     text_a = f.readline().strip()
#     text_b = f.readline().strip()

# python -X utf8 文本相似度.py < 04_3.txt

text_a = input()
text_b = input()

words1 = [word.strip() for word in text_a.split('|')]
words2 = [word.strip() for word in text_b.split('|')]

print("words1:", words1)
print("words2:", words2)


vector1 = {}
for word in words1:
    vector1[word] = vector1.get(word, 0) + 1

vector2 = {}
for word in words2:
    vector2[word] = vector2.get(word, 0) + 1

# 計算內積
dot_a_b = 0
for word, count in vector1.items():
    if word in vector2:
        dot_a_b += count * vector2[word]

# 計算向量A長度
len_a_sq = 0
for count in vector1.values():
    len_a_sq += count ** 2
len_a = len_a_sq ** 0.5

# 計算向量B長度
len_b_sq = 0
for count in vector2.values():
    len_b_sq += count ** 2
len_b = len_b_sq ** 0.5

if len_a == 0 or len_b == 0:
    similarity = 0.0
else:
    similarity = dot_a_b / (len_a * len_b)

print(similarity)