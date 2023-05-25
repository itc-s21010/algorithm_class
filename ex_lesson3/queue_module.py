import queue

MAX = 20

print("キュー")
q = queue.Queue()
for i in range(MAX):
    q.put(i)
for i in range(MAX):
    print(q.get(), end="から")

print("\n")
print("スタック")
s = queue.LifoQueue()
for i in range(MAX):
    s.put(i)
for i in range(MAX):
    print(s.get(), end="から")