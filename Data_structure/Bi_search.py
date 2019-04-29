def Binarysearch(a,l,r,x):
    if(r>=l):

        mid = int((r+l)/2)
        if a[mid]==x:
            return a[mid]
        elif a[mid]>x:
            return Binarysearch(a,l,mid-1,x)
        else:
            return Binarysearch(a,mid+1,r,x)

    else:
        return -1

num=[1,2,3,4,5,6,7,8,9]

rn=int(input())

rm=Binarysearch(num,0,8,rn)
print(rm)
            
        
