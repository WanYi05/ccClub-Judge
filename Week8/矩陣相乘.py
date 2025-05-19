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
