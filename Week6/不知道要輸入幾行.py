result = ""
try:
    while True:
        line = input()
        if not line:
            break
        result += line + "-"
except EOFError:
    pass

print(result.rstrip("-"))