num = int(input("Enter a number to check :- "))
if num>0:
    for i in range (2,num):
        if num%i==0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")
else:
    print("Enter a positive number")