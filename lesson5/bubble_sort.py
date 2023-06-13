	BLACK = '\033[30m'#(文字)黒
	RED = '\033[31m'#(文字)赤
	GREEN = '\033[32m'#(文字)緑
	YELLOW = '\033[33m'#(文字)黄
	BLUE = '\033[34m'#(文字)青
	MAGENTA = '\033[35m'#(文字)マゼンタ
	CYAN = '\033[36m'#(文字)シアン
	WHITE = '\033[37m'#(文字)白

data = [9, 4, 7, 2, 3, 8, 6, 1, 5, 0]
n = len(data)
print(data, "元のデータ")

for i in range(0, n-1):
    for j in range(0, n-1-i):
        if data[j] > data[j+1]:
            data[j], data[j+1] = data [j+1], data[j]
print(data, "ソート後のデータ")
print(f'CYAN', data)