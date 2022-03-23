n = int(input())
def func(n):
    if n==0:
        return 0
    else:
        print(n)
        func(n-1)
func(n)