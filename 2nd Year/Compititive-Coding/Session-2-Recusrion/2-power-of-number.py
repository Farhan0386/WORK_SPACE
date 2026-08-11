def power(base,pow):
    if pow==0:
        return 1
    elif pow==1:
        return base
    else:
        res=1
        res=res*power(base,pow+1)
        return res

print(power(2,3))
