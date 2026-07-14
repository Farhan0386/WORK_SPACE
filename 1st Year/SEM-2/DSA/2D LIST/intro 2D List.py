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

print(len(mat))
# for i in range(rowns):     to print the diagonal elements
#     print(mat[i][i],end=" ")
# print()

# to print edge elements
# for i in range(rowns):
#     for j in range(colns):
#         if i==0 or i==rowns-1 or j==0 or j==colns-1:
#             print(mat[i][j],end=" ")
#         else:
#             print(" ",end=" ")
#     print()


