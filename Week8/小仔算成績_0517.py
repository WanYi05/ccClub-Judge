total_str = input() 
num1_raw = total_str.split()
num1_list = [0 if int(num) == -1 else int(num) for num in num1_raw]

sorted_list = sorted(num1_list)

five = sorted_list[5:0:-1]

avg = sum(five) / 5 
hw = avg *(50/100)
if hw > 100:
    print(100)




test_str = input() 
num2_list = [100 if int(num) >100 else int(num) for num in test_str.split()]


score1 = num2_list[0] * (15/100)
score2 = num2_list[1] * (10/100)


final_score = int(input())
f_s = final_score * (25/100)


total_score = round((hw+score1+score2+f_s))
print(total_score)

list_grade = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'F', 'X']

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
    'X' : (0, 0)  
}

def get_grade(score_value):
    for grade, (low, high) in score.items():
        if low <= score_value <= high:
            return grade
    return 'Invalid'

grade = get_grade(total_score)



count_special = num1_raw.count('-1') 
shift = count_special * 2


if grade in list_grade:
    idx = list_grade.index(grade)
    new_idx = min(idx + shift, len(list_grade) - 1)
    grade = list_grade[new_idx]

print(grade)