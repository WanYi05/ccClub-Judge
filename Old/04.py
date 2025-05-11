s = ['A課程 報名人數/招生人數/費用:60/100/600', 'B課程 報名人數/招生人數/費用:23/30/200']
course = {}

for i in range(len(s)):
    sign_up_num = int(s[i].split(':')[1].split('/')[0])
    admissions_num = int(s[i].split(':')[1].split('/')[1])
    fee = int(s[i].split(':')[1].split('/')[2])
    schedule = str(round(sign_up_num / admissions_num * 100)) + '%'
    course[s[i].split()[0]] = [sign_up_num, admissions_num, schedule, fee]
    
print(course)

