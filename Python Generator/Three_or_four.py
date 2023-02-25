n = int(input())
def q():
    for i in range(n):
        yield i

for i in q():
    if i % 3 == 0 and i % 4 == 0:
        print(i, end = " ")