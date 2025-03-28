a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def cc(a, o, c):
    if o == "+":
        print(a, "+", c, "=", a+c)
    elif o == "-":
        print(a, "-", c, "=", a-c)
    elif o == "/":
        print(a, "/", c, "=", int(a/c))
    elif o == "*":
        print(a, "*", c, "=", a*c)
    else:
        print("False")

cc(a, o, c)