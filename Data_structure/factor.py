def factor(n):
    factor_list=[]

    for i in range(n):
        j=i+1
        if n%j==0:
            factor_list.append(j)
    return factor_list

def gcd(m,n):
    factor_list_m=factor(m)
    factor_list_n=factor(n)
    common_factor=[]
    for i in factor_list_m:
        for j in factor_list_n:
            if i==j:
                common_factor.append(i)
    last=len(common_factor)-1
    return common_factor[last]

def naive_gcd(m,n):
    cf=[]
    for i in range(1,min(m,n)+1):
        if m%i==0 and n%i==0:
            cf.append(i)
    return cf[-1]

def nolist_gcd(m,n):
    for i in range(1,min(m,n)+1):
        if m%i==0 and n%i==0:
            mrcf=i
    return mrcf

def scan_backward_gcd(m,n):
    i=min(m,n)
    while i>0 :
        if m%i==0 and n%i==0:
            return i
        else:
            i=i-1

#Euclid's algorithm
def euclid_gcd(m,n):
    #Assume m>=n
    if m<n:
        (m,n)=(n,m)
    while m%n!=0:
        diff=m-n
        # difference can be greater than n
        (m,n)=(max(diff,n),min(diff,n))
    return n

def recursive_gcd(m,n):
    #Assume m>=n
    if m<n:
        (m,n)=(n,m)
    if m%n==0:
        return(n)
    else:
        diff=m-n
        return gcd(max(diff,n),min(diff,n))

def best_gcd_algorithm(m,n):
    #Assume m>=n
    if m<n:
        (m,n)=(n,m)

    if m%n==0:
        return n
    else:
        return best_gcd_algorithm(n,m%n)
def best_gcd(m,n):
    if m<n:
        (m,n)=(n,m)
    while(m%n!=0):
        (m,n)=(n,m%n)
    return n

    
m,n=input().split()
m=int(m)
n=int(n)
k=best_gcd(m,n)
print(k)
            
