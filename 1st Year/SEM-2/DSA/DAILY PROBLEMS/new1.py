a=[4,0,5,-2,8,13,1,6]
for i in range(len(a)):
    ind =i
    for j in range(i+1,len(a)):
        if a[j]<a[ind]:
            ind = j
    a[i],a[ind]=a[ind],a[i]
print(a)