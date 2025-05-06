text = input()

a = text.split()

b = []

for c in a:
    key, value = c.split(" ")
    b.append((key, value))

result = dict(b)