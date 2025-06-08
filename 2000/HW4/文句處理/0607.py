keywords = ["apple", "app"]  # 先用固定的關鍵字方便示範

sentences = ["I have an apple"]  # 固定句子

for sentence in sentences:
    i = 0
    output = ""
    while i < len(sentence):
        matched = ""
        for kw in keywords:
            if sentence.startswith(kw, i):
                if len(kw) > len(matched):
                    matched = kw
        
        # 除錯訊息：顯示目前指標 i、找到的關鍵字 matched、目前結果 output
        print(f"i={i}, matched={matched}, output={output}")
        
        if matched:
            output += f'[{matched}]'
            i += len(matched)
        else:
            output += sentence[i]
            i += 1
    print("最後結果:", output)