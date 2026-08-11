def count(n):
    total=0
    while n!=0: 
        digit=n%10
        total+=digit
        n=n//10
    return total
print(count(6143))
print("By Recusrion")
def count1(n):
    if n==0 or n==1:
        return n
    return n%10 + count(n//10)
print(count1(6143))
