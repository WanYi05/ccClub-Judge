lines = []
total_sum = 0 

while True:
    line = input()
    if line == "end":
        break 

    if ',' in line:
        numeric_value = int(line.replace(',', '')) 

    else:
        numeric_value = int(line)
    
    total_sum += numeric_value 
        
total = format(int(total_sum), ",") 

print(total)