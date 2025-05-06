n = int(input())
student_grades = {}

for _ in range(n):
    student_id, grade_str = input().split()
    student_id = int(student_id)
    grade = int(grade_str)
    student_grades.setdefault(student_id, []).append(grade)

search_ids_input = input().split()
search_ids = [int(id) for id in search_ids_input]

total_grade = 0
found_count = 0

for search_id in search_ids:
    if search_id in student_grades:
        total_grade += sum(student_grades[search_id])
        found_count += len(student_grades[search_id])

if found_count > 0:
    average_grade = total_grade / found_count
    print(average_grade)