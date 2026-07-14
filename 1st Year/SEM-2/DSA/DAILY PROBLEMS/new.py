rowns=int(input("Enter the number of rows: "))
colns=int(input("Enter the number of columns: "))

mat=[]
for i in range(rowns):
    l1=[]
    for j in range(colns):
        var=int(input("Enter the element: "))
        l1.append(var)
    mat.append(l1)

for i in range(rowns):     
    for j in range(colns):
        print(mat[i][j],end=" ")
    print()
primary_diag = [] 
secondary_diag = [] 
for i in range(rowns): 
    primary_diag.append(mat[i][i]) 
    secondary_diag.append(mat[i][colns - 1 - i])

sum=0
for i in range(len(primary_diag)):
    sum+=primary_diag[i]
for i in range(len(secondary_diag)):
    sum+=secondary_diag[i]
if rowns == colns and rowns % 2 == 1: 
    mid = mat[rowns // 2][colns // 2] 
    sum -= mid

print(sum)