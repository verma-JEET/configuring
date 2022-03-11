ls1 = []
n = int(input("Enter the number of students :- "))
for i in range(n):
    ls = []
    name = input("Enter the name :- ")
    maths = input("Enter the marks of maths :- ")
    chemistry = input("Enter the marks of chemistry :- ")
    physics = input("Enter the marks of physics :- ")
    pps = input("Enter the marks of PPS :- ")
    foc = input("Enter the marks of FOC :- ")
    print("\n")
    ls.append(name)
    ls.append(maths)
    ls.append(chemistry)
    ls.append(physics)
    ls.append(pps)
    ls.append(foc)
    ls1.append(ls)
print(ls1)

max=ls1[0][1]
for j in range(n):
    if max<ls1[j][1]:
        max=ls1[j][1]
print(max," is max number in math's")

max=ls1[0][2]
for j in range(n):
    if max<ls1[j][2]:
        max=ls1[j][2]
print(max," is max number in chemistry")

max=ls1[0][3]
for j in range(n):
    if max<ls1[j][3]:
        max=ls1[j][3]
print(max," is max number in PHYSICS")

max=ls1[0][4]
for j in range(n):
    if max<ls1[j][4]:
        max=ls1[j][4]
print(max," is max number in PPS")

max=ls1[0][5]
for j in range(n):
    if max<ls1[j][5]:
        max=ls1[j][5]
print(max," is max number in FOC")