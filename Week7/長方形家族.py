# x1, y1, x2, y2, x3, y3, x4, y4 = int(input().split())
# print(x1)
# print(y1)
# print(x2)
# print(y2)
# print(x3)
# print(y3)
# print(x4)
# print(y4)


# x1=int(input())
# y1=int(input())
# x2=int(input()) 
# y2=int(input())
# x3=int(input()) 
# y3=int(input())
# x4=int(input()) 
# y4=int(input())

x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

if(x1==x3 and y1==y2 and x2==x4 and y3==y4 and (x2-x1)==(y1-y3)):
    print("正方形")

elif(x1==x3 and y1==y2 and x2==x4 and y3==y4 and (x2-x1)>(y1-y3)):
    print("長方形")
else:
    print("什麼也不是")
    # elif(x>0 and y>0):
    #     print("第一象限")
    # elif(x<0 and y>0):
    #     print("第二象限")
    # elif(x<0 and y<0):
    #     print("第三象限")
    # elif(x>0 and y<0):
    #     print("第四象限")
    # elif(x==0):
    #     print("y軸")
    # elif(y==0):
    #     print("x軸")

    # 進階版

line = input()
numbers_str = line.split()

if len(numbers_str) != 8:
    print("輸入的數字數量不正確，請輸入 8 個數字。")
else:
    try:
        numbers = [int(num_str) for num_str in numbers_str]
        x1, y1, x2, y2, x3, y3, x4, y4 = numbers

        if all(num < 10 for num in numbers):
            # 檢查 x 座標和 y 座標的對應關係
            if not (x1 == x3 and x2 == x4 and y1 == y2 and y3 == y4):
                print("什麼也不是")
            else:
                # 計算邊長
                width = abs(x2 - x1)
                height = abs(y1 - y3)

                # 檢查邊長是否為正數
                if width <= 0 or height <= 0:
                    print("什麼也不是")
                elif width == height:
                    print("正方形")
                else:
                    print("長方形")
        else:
            print("輸入的數字必須全部小於 10。")

    except ValueError:
        print("輸入包含非整數的值，請輸入整數。")
