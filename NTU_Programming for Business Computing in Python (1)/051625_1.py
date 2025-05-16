# q = 10 // 3
# mod = 10 % 3
# print(q, mod)
# # 3 1


a = int(input())

if 1 <= a <= 1000:
    k = 1000-a
    # print(k)
    v = k // 500
    b = k % 500
    # print(v, b)
    c = b // 100
    d = b % 100
    # print(c, d)
    e = d // 50
    f = d % 50
    # print(e,f)
    g = f // 10
    h = f % 10
    # print(g,h)
    i = h // 5
    j = h % 5
    # print(i,j)
    l = j // 1
    m = j % 1
    # print(l,m)
    print(v,c,e,g,i,l)
else:
    print("不正確")

