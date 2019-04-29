def Linearsearch(a,x):
    for i in a:
        if( i==x):
            return i
    return -1

num=[1,2,3,4,5,6,7,8,9]

r=22

rn=Linearsearch(num,r)
print(rn)
