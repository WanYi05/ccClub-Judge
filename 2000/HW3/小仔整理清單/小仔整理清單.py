# 讀入商品數 n 和交易數 m
n, m = map(int, input().split())

# 商品價格表
product_price = {}
for _ in range(n):
    name, price = input().split()
    product_price[name] = int(price)

# 顧客購買記錄 customer_record[顧客][商品] = 數量
customer_record = {}
# 商品被哪些顧客買過 product_customer[商品] = set(顧客)
product_customer = {}

for _ in range(m):
    cust, prod, qty = input().split()
    qty = int(qty)

    # 更新顧客購買記錄
    if cust not in customer_record:
        customer_record[cust] = {}
    if prod not in customer_record[cust]:
        customer_record[cust][prod] = 0
    customer_record[cust][prod] += qty

    # 更新商品對應的顧客
    if prod not in product_customer:
        product_customer[prod] = set()
    product_customer[prod].add(cust)

# 處理查詢指令直到 EOF（或空行）
while True:
    try:
        line = input()
        if not line:
            break
        parts = line.split()
        cmd = parts[0]

        if cmd == 'A':
            cust = parts[1]
            total = 0
            if cust in customer_record:
                for prod in customer_record[cust]:
                    total += customer_record[cust][prod] * product_price[prod]
            print(total)

        elif cmd == 'B':
            cust = parts[1]
            prod = parts[2]
            if cust in customer_record and prod in customer_record[cust]:
                print(customer_record[cust][prod])
            else:
                print(0)

        elif cmd == 'C':
            prod = parts[1]
            if prod in product_customer and product_customer[prod]:
                print(','.join(sorted(product_customer[prod])))
            else:
                print(0)

    except EOFError:
        break