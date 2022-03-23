n = int(input())
def func(n):
    if n>0 and n<10:
        return  1
    return 1 + func(n//10)
print(func(n))
func(n)