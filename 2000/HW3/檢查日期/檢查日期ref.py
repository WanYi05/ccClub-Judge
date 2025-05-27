lines = []
total_sum = 0

while True:
    line = input()
    if line == "end":
        break
    
    else:
        num_list = int(line)
    
    total_sum = total_sum + num_list
    lines.append(line)

print(total_sum)
