# 必須要是cmd
# cd 資料夾路徑
# python 程式碼(含副檔名) < 資測txt檔案
#
# 如下
# C:\Users\Wan\Desktop\ccClub Judge\Week8>python 矩陣相乘.py < 03_2.txt
# [523669010, 276189240, 1186616700, 625407500]


n = int(input())

matrices = []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    matrices.append([[a, b], [c, d]])

result = matrices[0]

for i in range(1, n):
    A = result
    B = matrices[i]

    r00 = A[0][0]*B[0][0] + A[0][1]*B[1][0]
    r01 = A[0][0]*B[0][1] + A[0][1]*B[1][1]
    r10 = A[1][0]*B[0][0] + A[1][1]*B[1][0]
    r11 = A[1][0]*B[0][1] + A[1][1]*B[1][1]

    result = [[r00, r01], [r10, r11]]

print([result[0][0], result[0][1], result[1][0], result[1][1]])
