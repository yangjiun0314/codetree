a, b = map(int, input().split())

# Please write your code here.  
def contains_369(n):
    # 계속 10으로 나눠주며
    # 일의 자리를 조사합니다.
    while n > 0:
        if n % 10 == 3 or n % 10 == 6 or n % 10 == 9:
            return True

        n //= 10

    return False


# 3, 6, 9를 포함하거나 3의 배수인지를 판단합니다.
def is_369_number(n):
    return contains_369(n) or (n % 3 == 0)


cnt = 0
for i in range(a, b + 1):
    if is_369_number(i):
        cnt += 1

print(cnt)