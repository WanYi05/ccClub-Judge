# 1
# str asdf
# str str str str

n = int(input())         #請輸入要創建的字典數量：
dictionaries_list = []

for i in range(n):
    text = input() #f"請輸入第 {i+1} 個字典的鍵和值 (key value)："
    parts = text.split()
    if len(parts) == 2:
        key = parts[0]
        value = parts[1]
        new_dict = {key: value}
        dictionaries_list.append(new_dict)
    else:
        print(f"第 {i+1} 個輸入 '{text}' 格式不正確，請輸入一個鍵和一個值（以空格分隔）。")

# print(dictionaries_list)


# 第2行：輸入要查詢的 key
query = input()
query_words = query.split()
found_values = []

for word in query_words:
    found = False
    for dictionary in dictionaries_list:
        if word in dictionary:
            found_values.append(dictionary[word])
            found = True
            break  # 找到一個匹配的單詞後，可以跳出內層迴圈
    if not found:
        print(f"單字 '{word}' 不存在")
        found_values = [] # 如果有單字不存在，清空已找到的值
        break # 只要有一個單字不存在，就停止查找

if found_values:
    print(" ".join(found_values))


# Answer 簡單版
# n = int(input())
# translation_dict = {}

# for i in range(n):
#     source, target = input().split()
#     translation_dict[source] = target

# query = input().split()
# translated_words = [translation_dict[word] for word in query]
# print(" ".join(translated_words))