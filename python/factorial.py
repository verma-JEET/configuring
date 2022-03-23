n = int(input("Enter a number to find its Factorial :- "))
fact = 1
i=1
if n<0 :
    print("Enter a positive number.")
elif n==0 :
    print("Factorial of 0 is 1")
else:
    for i in range (1,n + 1):
        fact = fact*i
print(fact)