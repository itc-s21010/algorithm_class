import queue

MAX = 7

node = ["赤", "橙", "黃", "緑", "青", "藍", "紫"]

print(node)
q = queue.Queue()
for i in range(MAX):
    print(node[i], end="→")
print('\n')
for i in reversed(node):
    print(i, end="→")