def count_numbers(nums): 

    counts = {} 

    for num in nums: 

        if num in counts: 
            counts[num] += 1
        else:
            counts[num] = 1

    return counts

# n = int(input("請輸入行數: "))
n = int(input())
all_nums = []

# for _ in range(n):
#     line = list(map(int, input().split()))
#     line.sort()          
#     print("排序後的數字:", line) 
#     all_nums.extend(line)  

for i in range(n):
    line = list(map(int, input().split()))
    line.sort()          
    print(f"第{i+1}行排序後的數字:", line)  
    all_nums.extend(line)   

result = count_numbers(all_nums)

print("所有數字出現次數：")
# for num, count in sorted(result.items()):
for num, count in sorted(result.items(), key=lambda x: x[1], reverse=True):
    print(f"數字 {num} 出現了 {count} 次")
