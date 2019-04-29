def s(x):
    return(x*x)

def apply(s,x,n=2):
    res=x
    for i in range(n):
        res=s(res)
    return(res)

print(apply(s,5))

def iseven(x):
    return(x%2==0)
def square(x):
    return(x*x)

print(list(map(square,filter(iseven,range(0,100)))))

list=[square(i) for i in range(0,10) if iseven(i)]
print(list)

list1=[(x,y,z) for x in range(100) for y in range(x,100) for z in range(y,100) if x*x + y*y == z*z ]
print(list1)
