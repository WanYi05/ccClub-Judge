keywords = input().split()

keywords.sort(key=len, reverse=True)

lines = []
while True:
    line = input()
    if line == "end":
        break
    lines.append(line)

for line in lines:
    i = 0
    output = ""
    while i < len(line):
        matched = ""
        for kw in keywords:
            if line.startswith(kw, i):

                if len(kw) > len(matched):
                    matched = kw
        if matched:
            output += f"「{matched}」"
            i += len(matched)
        else:
            output += line[i]
            i += 1
    print(output)