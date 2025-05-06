a = set()
b = set([1,2,3,4,5,1,2,3,4,5])
c = set({'x':1,'y':2,'z':3})
d = set('hello')
print(a)   # set()
print(b)   # {1, 2, 3, 4, 5}  只留下不重複的部分
print(c)   # {'x', 'y', 'z'}  如果是字典，只保留鍵
print(d)  

for i in range (0,8,1):
    print(i, end="")
