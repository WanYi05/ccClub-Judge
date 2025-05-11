n = input().split(",")

list_n = [int(i) for i in n]

sorted_n = sorted(list_n, reverse=True)

k=0

for i in range(len(n)):
    if list_n[i]!=sorted_n[i]:
        k+=1

print(f"過來一下，你又端錯{k}次")