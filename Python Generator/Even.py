n = int(input())
def w():
    for i in range(n):
        yield i

for i in w():
    if i % 2== 0:
        print(i, end = " ")


