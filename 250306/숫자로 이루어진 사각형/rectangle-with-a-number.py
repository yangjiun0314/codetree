def print_num_rect(n):
    count = 0
    for _ in range(n):
        for _ in range(n):
            count += 1
            if count == 10:
                count = 1
            print(count, end=" ")
        print()

n = int(input())
print_num_rect(n)

# Please write your code here.