def find_a(n, m):
    s = m if m > n else n
    for i in range(1, s):
        if n%i == 0:
            
            if m%i == 0:
                s = i
    print(s)

n, m = map(int, input().split())

find_a(n, m)
# Please write your code here.