a = input()

eng = any(c.isalpha() for c in a)   # 檢查有沒有字母
num = any(c.isdigit() for c in a)   # 檢查有沒有數字

if eng and num:
    print("True")                  # 同時有字母和數字
else:
    print("False")                 # 只有字母或只有數字或其他符號