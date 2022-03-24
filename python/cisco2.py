r1 = int(input("enter the number of rows for first matrix"))
c1 = int(input("enter the number of column for first matrix"))
matrix = []
for i in range(r1):
    a=[]
    for j in range(c1):
        a.append(int(input()))
    matrix.append(a)
print("elements of first matrix")
for i in range(r1):
    for j in range(c1):
        print(matrix[i][j])
    print()