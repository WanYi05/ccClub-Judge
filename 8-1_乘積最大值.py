def max_mul(l):
    s = []  # 建立空清單以放進乘積值
    for i in range(len(l) - 1):
        multi_value = int(l[i]) * int(l[i + 1])  # 相鄰兩數相乘
        s.append(multi_value)  # 將乘積加入清單
    return max(s)  # 傳回乘積中的最大值

# multi_int = input("請輸入一串數字（以空格分隔）: ")
multi_int = input()
thebest = multi_int.split()
print(max_mul(thebest))