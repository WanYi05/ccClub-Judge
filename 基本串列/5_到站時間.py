# 1 Ans (會出現 25:54 之類的bug)
start_time = input() #15:32
add_min = int(input()) #37

start_time1 = start_time.split(":") #['15', '32']

hour = add_min // 60 # quotient : 32/60 = 0 商

min = add_min % 60 # remainder : 32/60 = 32 餘數

end_time1 = int(start_time1[0]) + int(hour) # 時: 15 + 0
end_time2 = int(start_time1[1]) + int(min) # 分: 32 + 37

hour1 = int(end_time2) // 60 # 分 69/60 = 1 商
min1 = int(end_time2) % 60  # 分 69/60 = 9

end_time1 = int(end_time1) + int(hour1) # 時: 15 + 1

print(end_time1, min1)