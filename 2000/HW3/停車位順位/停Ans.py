n = int(input())

residents_data = []

for i in range(n): 
    resident_info = input().split()
    residents_data.append(resident_info + [i])

building_priority = {'A': 1, 'B': 2, 'C': 3}

def seniority_priority(years):
    years = int(years) 
    if years >= 10:
        return 1
    elif years >= 5:
        return 2
    else: 
        return 3

def address_priority(address):
    address = int(address) 
    if address % 2 != 0: 
        return 1
    else: 
        return 2

sorted_residents = sorted(residents_data, key=lambda resident: (
    building_priority[resident[1]],  
    seniority_priority(resident[2]),         
    address_priority(resident[3]),           
    resident[4]                               
))

for resident in sorted_residents:
    print(resident[0]) 