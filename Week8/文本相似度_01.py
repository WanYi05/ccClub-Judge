num1 = 3
num_sqrt1 = num1 ** 0.5
print(' %0.3f 的平方根为 %0.3f' % (num1 ,num_sqrt1))

num2 = 7
num_sqrt2 = num2 ** 0.5
print(' %0.3f 的平方根为 %0.3f' % (num2 ,num_sqrt2))

# 正確的計算方式，直接使用數值進行運算
c = 2 / (num_sqrt1 * num_sqrt2)

print(f"c 的值為: {c}")