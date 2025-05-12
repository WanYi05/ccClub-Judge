# Example
# def to_binary(n):
#     # do something to transfer n to binary, and return your answer
#     # ans should be list of integers
#     return ans

# 1

# def to_binary(n):
#     remainders = []
#     while n > 0:
#         remainders.append(n % 2)
#         n = n // 2
#     remainders.reverse()
#     return ''.join(map(str, remainders))

# # 讓使用者輸入一個整數，並轉成 int
# user_input = int(input())

# # 呼叫函式並印出結果
# print(to_binary(user_input))


def to_binary(n):
    b = bin(n)[2:]  # 去掉 '0b' 前綴
    result = [int(b[0])]  # 第一位一定保留
    for ch in b[1:]:
        if int(ch) != result[-1]:
            result.append(int(ch))
    return result

a = int(input())

print(to_binary(a))