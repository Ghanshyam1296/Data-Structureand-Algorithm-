import math

def Jp_search(a,n,x):
    #calculating step size
    jump=math.sqrt(n)
    prev=0

    while(a[int(min(jump,n-1))]<x):
        prev=jump
        jump+=math.sqrt(n)

        if (prev>=n):
            return -1

    while(a[int(prev)]<x):
        prev+=1

        if(prev==min(jump,n)):
            return -1

    if(a[int(prev)]==x):
        return prev

    return -1

num =[1,2,3,4,5,6,7,8,9]
h=int(input())
result=Jp_search(num,len(num),h)

print(result)
        
    
    
    
