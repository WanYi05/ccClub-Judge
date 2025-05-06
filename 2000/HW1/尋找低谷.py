n = input()
min_num = [int(i) for i in n.split()]

for i in range(1, len(min_num) - 1):  
    if min_num[i] < min_num[i - 1] and min_num[i] < min_num[i + 1]:
        print(i)
        break  # 因為保證只有一個低谷，找到後就可以停止迴圈