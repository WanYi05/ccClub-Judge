# 4 4
n, m = map(int, input().split())

# apple 30
# orange 40
# pizza 150
# egg 10

product_price = {}
for _ in range (n):
    name, price = input().split()
    product_price[name] = int(price) # product_price["apple"] = 30

    # 補充
    # 相反，如果是讀取某個商品的值
    # price = product_price['apple']  #30


# Jeffery apple 10
# Anny orange 20
# Jeffery orange 15
# Anny apple 2

# 顧客購買記錄 
# customer_record[顧客][商品] = 數量
customer_record = {}

# 商品被哪些顧客買過 
# product_customer[商品] = set(顧客)
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