all_number_lists = []

datedict = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

while True:
    line = input()

    if line == "end":
        break
    
    cleaned_line = line.replace(" ", "")
    num_list = [int(num) for num in cleaned_line.split(',')]
    
    if len(num_list) != 3:
        print("error")
        continue 

    year = num_list[0]
    month = num_list[1]
    day = num_list[2]

    if year > 0:

        if 1 <= month <= 12:
            max_days_in_month = datedict[month]
            
            if 1 <= day <= max_days_in_month:
                print("OK")
                
                all_number_lists.append(num_list) 
            else:
                print("error") 
        else:
            print("error") 
    else:
        print("error") 