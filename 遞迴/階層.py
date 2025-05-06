# n!
# 3! = 1*2*3 

# n*(n-1)*(n-2)
# 結束條件: 當你n=1的時候 就會結束這個迴圈

#4! = 4 * 3 * 2 * 1
#(4 * 6)
#     (4-1 * 2)
#          (4 - 2 * 1)
#               * 4-3 ))    -->終止條件  

def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)

# value = 4
ans = factorial(6)
print(ans)


# def factorial(n):
#     temp = n
#     while(temp>1):
#         n = n * (temp-1)
#         temp = temp-1
#     return