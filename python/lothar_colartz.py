no = int(input("Enter a positive number : "))
print(no)
step=1
while no!=1:
    if no%2==0:
        no=no//2
        print(no)
    else:
        no=3*no+1
        print(no)
    step+=1
print("steps =",step)