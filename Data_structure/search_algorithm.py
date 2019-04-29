#Search Algorithm
#Binary serach is applicable for only sorted list
#list in the python is list but here we are pretending it as array

def binary_search(seq,v,l,r):
    if(l-r==0):
        return(False)
    mid=l+r//2 #integer division
    if(seq[mid]==v):
        return(seq[mid])
    elif(seq[mid]<v):
        return binary_search(seq,v,l,mid)
    else:
        return binary_search(seq,v,mid+1,r)

seq=[1,2,3,4,5,6,7,8]

print(binary_search(seq,10,0,len(seq)))

def linear_search(seq,v):
    pos=0
    for i in seq:
        if(i==v):
            return(pos)
        pos=pos+1
    return(False)

seq1=[1,2,3,4,5,6,4]
print(linear_search(seq1,4))

def selection_sort(seq):
    for i in range(len(seq)):
        minpos=i
        for j in range(minpos,len(seq)):
            if seq[j]<seq[minpos]:
                minpos=j
                (seq[i],seq[minpos])=(seq[minpos],seq[i])
    return seq

def insertion_sort(seq):
    for i in range(len(seq)):
        sliceend=i
        while sliceend>0 and seq[sliceend]<seq[sliceend-1]:
            (seq[sliceend],seq[sliceend-1])=(seq[sliceend-1],seq[sliceend])
            sliceend=sliceend-1
    return seq

list1=[2,5,3,7,8,1,8,1]
print(insertion_sort(list1))

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

def multiply(m,n):
    if n==1:
        return(m)
    else:
        return m+multiply(m,n-1)

print(multiply(5,4))

def merge(A,B):
    (C,m,n)=([],len(A),len(B))
    (i,j)=(0,0)
    while i+j<m+n:
        if i==m:
            C.append(B[j])
            j=j+1
        elif j==n:
            C.append(A[i])
            i=i+1
        elif A[i]>B[j]:
            C.append(B[j])
            j=j+1
        elif A[i]<=B[j]:
            C.append(A[i])
            i=i+1
    return C

def mergesort(A,left,right):
    if right-left<=1:
        return A[left:right]
    if right-left>1:
        mid=(left+right)//2

        L=mergesort(A,left,mid)
        R=mergesort(A,mid,right)
        return merge(L,R)

def quicksort(A,l,r):
    if r-l<=1:
        return()
    yellow=l+1
    for green in range(l+1,r):
        if A[green]<=A[l]:
            (A[green],A[yellow])=(A[yellow],A[green])
            yellow=yellow+1
        (A[l],A[yellow-1])=(A[yellow-1],A[l])

        quicksort(A,l,yellow-1)
        quicksort(A,yellow,r)
    return(A)

        

l1=[2,5,4,3,1,10,1,9,8]
print(quicksort(l1,0,len(l1)))


        
