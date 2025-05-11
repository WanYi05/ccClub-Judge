# 給定一個十進位的正整數 n，請試著用 while loop 轉換二進位，並輸出最後的二進位結果。
# n = int(input())

# ans = ""               # 儲存結果的字串

# while n > 0:
#     remainder = n % 2     # 把餘數取出來（0 或 1）
#     ans = str(remainder) + ans   # 往前加到結果中
#     n = n // 2            # 整數除以 2

# print(ans)





n = int(input()) 

ans = ""  # 儲存解果的字串

while n > 0:
    r = n % 2 # r: 餘數(整數) 餘數取出來 可能為0或1
    ans = str(r) + ans # r 餘數(整數)轉為字串，往前儲存
    n = n // 2  #整數再除以2

print(ans)




# 給定一個十進位的正整數 n，請試著用 while loop 轉換二進位，並輸出最後的二進位結果。

n = int(input())

ans = ""

while n > 0:
    remainder = n % 2 #結果為0或1
    ans = str(remainder) + ans
    n = n // 2 # n繼續除以2

print (ans)
      




