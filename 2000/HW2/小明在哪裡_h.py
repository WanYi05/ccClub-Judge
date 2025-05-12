def find_ming():
    data=[]
    while True:
        try:
            row = input()
            if row.strip()=='':
                break
            data.append(row.strip().split())
        except EOFError:
            break
    for row_index,row in enumerate(data):
        if '小明' in row:
            col_index = row.index('小明')
            return (row_index,col_index)
    return None
position = find_ming()
if position:
    print(position)