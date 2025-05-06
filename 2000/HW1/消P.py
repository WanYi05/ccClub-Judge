# 紫藍藍紅紅紫綠 -> 紫紅紅紫綠 -> 紫紫綠 -> 綠

gem = list(input())

n = 0

while n < len(gem) -1:
    if gem[n] == gem[n+1]:
        gem.pop(n)
        gem.pop(n)
        n = 0
    else:
        n = n + 1
if len(gem) > 0:
    print("".join(gem))
 

s = input()
n = []

for i in s:
    if n and n[-1] == i:
        n.pop()
    else:
        n.append(i)

print("".join(n))