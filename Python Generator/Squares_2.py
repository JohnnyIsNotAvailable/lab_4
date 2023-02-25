a = int(input())
b = int(input())
def sq():
    for i in range(a , b):
        yield i

for i in sq() :
    ans = i * i
    print(ans, end = " ")
