# 1 Score Tuple (Packing, Unpacking)
# score = {
#     'A+': (90, 100),
#     'A': (85, 89),
#     'A-': (80, 84),
#     'B+': (77, 79),
#     'B': (73, 76),
#     'B-': (70, 72),
#     'C+': (67, 69),
#     'C': (63, 66),
#     'C-': (60, 62),
#     'F': (0, 59),
#     'X': 0
# }
# def get_grade(score_value):
#     for grade, (low, high) in score.items():
#         if low <= score_value <= high:
#             return grade
#     return 'Invalid'

# print(get_grade(float(input())))


# 2. 作業
total_str = input() #請輸入多個數字，以空格分隔：
num1_raw = total_str.split()
num1_list = [0 if int(num) == -1 else int(num) for num in num1_raw]

sorted_list = sorted(num1_list)
# print(sorted_list)


# 取前五個數字
five = sorted_list[5:0:-1]
# print(five)
# 計算平均（浮點數）
avg = sum(five) / 5 #平均值（浮點數
hw = avg *(50/100)
if hw > 100:
    print(100)
# print("作業百分比", hw)


# 3. 期中考成績

test_str = input() #"請輸入2個數字，以空格分隔："
num2_list = [100 if int(num) >100 else int(num) for num in test_str.split()]
# print(num2_list)

score1 = float(num2_list[0] * (15/100))
# print(score1)

score2 = float(num2_list[1] * (10/100))
# print(score2)

# 3. 期末專案成績

final_score = int(input())
f_s = final_score * (25/100)
# print(f_s)


sum = round((hw+score1+score2+f_s))
print(sum)

list_grade = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'F', 'X']

# 假設 score 的區間如下（你可根據需要修改）
score = {
    'A+': (90, 100),
    'A' : (85, 89),
    'A-': (80, 84),
    'B+': (77, 79),
    'B' : (73, 76),
    'B-': (70, 72),
    'C+': (67, 69),
    'C' : (63, 66),
    'C-': (60, 62),
    'F' : (1, 59),
    'X' : (0)  # 假設 X 是不合理分數
}

def get_grade(score_value):
    for grade, (low, high) in score.items():
        if low <= score_value <= high:
            return grade
    return 'Invalid'


# 取得原始成績
grade = get_grade(sum)


# 尋找 -1 的數量
count_special = num1_raw.count('-1')  # 注意是字串 '-1'
shift = count_special * 2

# 平移成績等級
if grade in list_grade:
    idx = list_grade.index(grade)
    new_idx = min(idx + shift, len(list_grade) - 1)
    grade = list_grade[new_idx]

print(grade)