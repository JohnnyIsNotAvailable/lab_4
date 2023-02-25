def down(i):
    while i >= 0:
        yield i
        i -= 1
        
n = int(input())
for num in down(n):
    print(num)