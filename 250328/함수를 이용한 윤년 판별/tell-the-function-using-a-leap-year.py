y = int(input())

# Please write your code here.
def yoonyear(n):
    if n % 100 == 0 and n % 400 != 0:
        return False
    if n % 4 == 0:
        return True
    return True

if yoonyear(y) == True:
    print("true")
else:
    print("false")