def find_a(n, m):
    s = m if m > n else n
    a = 0
    for i in range(1, s+1):
        if n%i == 0:
            if m%i == 0:
                a = i
    print(a)

n, m = map(int, input().split())

find_a(n, m)
# Please write your code here.