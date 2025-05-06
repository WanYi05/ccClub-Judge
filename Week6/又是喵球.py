s = input()
result = ""

for ch in s:
    if ch.upper() in "ABCDEFGHIJKLM":
        result += ch.upper()
    else:
        result += ch.lower()

print(result)