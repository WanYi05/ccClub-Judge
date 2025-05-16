w = int(input())
x = int(input())
y = int(input())
z = int(input())

if 0<=w<=10 or 0<=x<=10 or 0<=y<=10 or 0<=z<=10:
    print((w*50)+(x*10)+(y*5)+(z*1))
else:
    print("非預期結果")  