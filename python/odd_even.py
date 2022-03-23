n = int(input("Enter a number from to find odd and even numbers :- "))
print("Even number's are :- ")
for n in range (1,n+1):
    if n%2==0:
        print(n)

print("\nOdd numbers are :- ")
for n in range (1,n+1):
    if n%2 != 0:
        print(n)