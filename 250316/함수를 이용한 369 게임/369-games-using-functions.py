a, b = map(int, input().split())

# Please write your code here.  
def game369(n):
    return ((n%10 == 3) or (n//10 == 3)) or ((n%10 == 6) or (n//10 == 6)) or ((n%10 == 9) or (n//10 == 9)) or ((n%100 == 3) or (n//100 == 3)) or ((n%100 == 6) or (n//100 == 6)) or ((n%100 == 9) or (n//100 == 9))
def game(n):
    return n%3 == 0 or game369(n)
cnt = 0
for i in range(a, b+1):
    if game(i):
        cnt += 1

print(cnt)