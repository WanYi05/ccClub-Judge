# 計算機語音
# 小明的計算機非常高科技，能夠在算出結果之後，選擇語音功能，計算機會把數字一個字一個字的唸出來

# 但是現在計算機沒電了，你能夠幫他寫一個程式做到這件事嗎？

# 舉例來說輸入 1、2、3 代表數字 123，現在我們希望能把輸入的數字 +1 也就是變成 124 ，再把結果以串列方式個別輸出

# 1,2,3 -- > [1, 2, 4]
# 4,3,2,1 -- > [4, 3, 2, 2]

# 1. 思考邏輯1
# lst1 = input() #1,2,3

# # a = lst1.split(",") # 結果為字串: '1', '2', '3'
# a = map(int, lst1.split(","))
# print(type(a))


# 補充:
# #輸入lst1的值1 -> True 非則False
# s = int(input())

# if s in a:
#     print("True")
# else:
#     print("False")


# text = input()              # 例如輸入：4,3,2,1
# parts = text.split(",")     # 把字串分割成列表
# new_num = "".join(parts)     # 把列表合併成一個新的字串
# result = int(new_num)        # 把字串轉成整數
# print(result+1)               # 印出結果為數字

# parts = text.split(",")      # 這裡可以不用 split，因為你直接輸入一串數字

# new_num = "".join(parts)     # 合併（如果原本有用逗號隔開）
# result = int(new_num)        # 轉成整數
# result += 1                  # 加一，這時變成 10000

# # 把整數轉回字串後，用 list() 拆開成每個字元
# digits = list(str(result))
# print(digits)


# EX2
text = input()              # 例如輸入：4,3,2,1
parts = text.split(",")     # 把字串分割成列表 ['4', '3', '2', '1']
new_num = "".join(parts)    # 合併成字串 '4321'
result = int(new_num)       # 轉成整數 4321

# print(result + 1)           # 印出結果為數字（加1後）

# 加1後的數字再拆開成字元，變成 list
digits = [int(d) for d in str(result + 1)]
print(digits)       