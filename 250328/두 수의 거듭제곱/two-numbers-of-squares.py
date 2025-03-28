a, b = map(int, input().split())

# Please write your code here.
def times(a, b):
    result = a
    for i in range(b-1):
        result = result * a
    return result

print(times(a, b))