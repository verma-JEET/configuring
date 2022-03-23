n = int(input("Enter the number of rows :- "))
for i in range (n):
    for j in range (i):
        print("*",end=" ")
    print("\n")

for k in range (n-2,0,-1):
    for l in range (k):
        print("*",end=" ")
    print("\n")