# 初始輸入一串整數

a = list(map(int, input().split()))  # 初始帳目


# 輸入一個指令
# 例如輸入：r 204

while True:
    cmd = input().split()

    if len(cmd) == 0:
        continue
    
    # 若輸入為 "a 4"，請在帳目中加入 4 這個數字。

    if cmd[0] == "a" and len(cmd) > 1:
        try:
            a.append(int(cmd[1]))
        except ValueError:
            pass

    # 若輸入為 "r 204"，請從帳目中刪除第一次出現 204 這個數字，若帳本中沒有 204 這個數字，則略過這個指令。

    elif cmd[0] == "r" and len(cmd) > 1:
        try:
            val = int(cmd[1])
            if val in a:
                a.remove(val)
        except ValueError:
            pass

    # 若輸入為 "p -1"，請從帳目中刪除 index 為 -1 的帳目，p 指令後如果是負數，保證是 -1。
    # 若輸入為 "p 2" ，請從帳目中刪掉 index 為 2 的帳目，若 index 2 不存在帳本中，則略過這個指令。

    elif cmd[0] == "p" and len(cmd) > 1:
        try:
            index = int(cmd[1])
            if index == -1 and len(a) > 0:
                a.pop(-1)
            elif 0 <= index < len(a):
                a.pop(index)
        except ValueError:
            pass

    # 若輸入為 "q 4" ，請結束輸入的部分，並印出 index 為 4 的內容，以及所有帳目的平均數；若該 index 不存在，請輸出Error，並且不需要輸出平均數。 
    elif cmd[0] == "q" and len(cmd) > 1:
        try:
            index = int(cmd[1])
            if 0 <= index < len(a):
                print(a[index])
                avg = sum(a) / len(a)
                print(int(avg))  # 無條件捨去
                break
            else:
                print("Error")
                break
        except ValueError:
            print("Error")
            break

    # 每次指令後印出帳本
    # print("目前帳目：", a)
