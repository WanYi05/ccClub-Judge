# def func(n, remainders=[]):
#     remainder = n % 26
#     quotient = n // 26

#     remainders.append(remainder)  # 先記錄餘數

#     if quotient == 0:
#         return remainders
#     else:
#         return func(quotient, remainders)

# n = int(input())

# all_remainders = func(n)
# print(f"{all_remainders}")

# def func(n):
#     remainders = []
#     quotients = []

#     # print(f"初始 n: {n}")
#     while n >= 26:
#         remainder = n % 26
#         quotient = n // 26
#         remainders.append(remainder)
#         quotients.append(quotient)
#         n //= 26
#         # print(f"n: {n}, remainders: {remainders}, quotients: {quotients}")

#     # print(f"迴圈結束，n: {n}, remainders: {remainders}, quotients: {quotients}")
#     if quotients:
#         result = [n] + remainders[::-1]
#     else:
#         result = [n]
#     # print(f"最終結果: {result}")
#     return result

# n = int(input())
# final_result = func(n)
# print(f"{final_result}")

# dict = { 
#     'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
#     'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 
#     'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 
#     'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
# }

def func(n):
    remainders = []
    quotients = []

    while n >= 26:
        remainder = n % 26
        quotient = n // 26
        remainders.append(remainder)
        quotients.append(quotient)
        n //= 26

    if quotients:
        result = [n] + remainders[::-1]
    else:
        result = [n]
    return result

n = int(input())
final_result = func(n)
# print(f"{final_result}")

dict = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G',
    7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N',
    14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
    20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'
}

output_string = ""
for num in final_result:
    if num in dict:
        output_string += dict[num]

print(output_string)
