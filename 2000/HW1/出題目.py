def math_questions(w, a, s, r):
    if w - a == 0:
        if r - a * s == 0:
            return None  
        else:
            return None
    else:
        x = (r - a * s) / (w - a)
        y = (w * s - r) / (w - a)
        if x > 0 and y > 0 and x == int(x) and y == int(y):
            return (int(x), int(y))  
        else:
            return None

w = int(input())
a= int(input())
xy_sum = int(input())
result = int(input())

solution = math_questions(w, a, xy_sum, result)

if solution:
    x_calculated, y_calculated = solution
    print("True")
else:
    print("False")