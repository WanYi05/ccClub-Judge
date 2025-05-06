line = input().split()
start = int(line[0])
limit = int(line[1])
diff = int(line[2])

sequence = []
current = start
sum_val = 0

while current < limit:
    sequence.append(current)
    sum_val += current
    current += diff

print(*sequence)
print(sum_val)
