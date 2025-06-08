#以空白字元切割成多個子字串(串列元素)，變成字串列表
keywords = input().split()

#字串長度由長到短
#Input: app apple nice
#Output: ['apple', 'nice', 'app']
keywords.sort(key = len, reverse = True)

# print(keywords)

lines=[]

while True:
    line = input()
    if line == "end":
        break
    lines.append(line)

for line in lines:
    result = ""
    i = 0
    while i < len(line):
        matched = False
        for word in keywords:
            word_len = len(word)
            if line[i:i + word_len] == word:
                result = result + "[" + word + "]"
                i = i + word_len
                matched = True
                break
        if not matched:
            result = result + line [i]
            i = i + 1
    print(result)
