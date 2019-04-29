def InterpolationSearch(a,n,x):
    l=0
    h=n-1

    pos=l+(((x-a[l])*(h-l))/(a[h]-a[l]))

    while l<=h and x>a[l] and x<a[h]:
        if a[int(pos)]==x:
            return int(pos)
        if a[int(pos)]>x:
            h=int(pos)-1
        else:
            l=int(pos)+1

    return -1

num=[1,2,3,4,5,6,7]

r=int(input())
result=InterpolationSearch(num,len(num),r)
print(result)
    
    
        
