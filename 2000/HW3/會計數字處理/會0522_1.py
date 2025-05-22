lines = []
print()
while True:
    line = input()
    if line == "end":
        break  # 當輸入 'end' 時，跳出迴圈
    lines.append(line)

print()
for l in lines:
    print(l)