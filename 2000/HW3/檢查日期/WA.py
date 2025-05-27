n = []

while True:
    s = input()
    if s == "end":
        break

    try:
        year_str, month_str, day_str = s.split(',')
        year = int(year_str)
        month = int(month_str)
        day = int(day_str)

        if month < 1 or month > 12:
            n.append("error")
            continue

        days_in_month = {
            1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }

        if day < 1 or day > days_in_month[month]:
            n.append("error")
        else:
            n.append("OK")

    except EOFError:
        n.append("error")
for i in range(len(s)-1):
    print(n[i])