a, b = map(int, input().split())

# Please write your code here.
def sm(n):
    for i in range(2, n):
        if n % i == 0:
            return 0
    return n

cnt = 0
for i in range(a, b+1):
    if sm(i) == 1:
        continue
    cnt += sm(i)
print(cnt)