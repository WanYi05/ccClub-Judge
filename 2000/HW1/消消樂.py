# 紫藍藍紅紅紫綠 -> 紫紅紅紫綠 -> 紫紫綠 -> 綠

s = input()
list_1 = []

for char in s:
    if list_1 and list_1[-1] == char:
        list_1.pop()  # 如果和上個一樣，就消掉上個
    else:
        list_1.append(char)  # 否則就加進來

print("".join(list_1)) #將子字符串連成字符串了