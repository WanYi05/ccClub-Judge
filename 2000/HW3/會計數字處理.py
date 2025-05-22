lines = []
total_sum = 0 

while True:
    line = input()
    if line == "end":
        break  
    
    try:
        if ',' in line:
            numeric_value = int(line.replace(',', '')) 

        else:
            numeric_value = int(line)
        
        total_sum += numeric_value 
        lines.append(line) 
        
    except ValueError:
        print("錯誤")

total = format(int(total_sum), ",") 

print(total)