n = int(input("Enter a number to find sum of all odd number :- "))
sum = 0
print("Sum of odd numbers is :-")
for n in range (1,n+1):
    if n%2 != 0:
        sum=sum+n
print(sum)
