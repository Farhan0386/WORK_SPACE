n=[2,3,7,3,2,1,4]
def duplicate(arr):
    ans=[]
    for i in range(len(arr)):
        for j in range(len(ans)):
            if ans[j]==arr[i]:
                break
        else:
            ans.append(arr[i])
    return ans
print(duplicate(n))