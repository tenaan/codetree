n = int(input())

def p_hello(n):
    if n == 0:
        return
    p_hello(n - 1)
    print("HelloWorld")

p_hello(n)