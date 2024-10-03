# Time Complexity:
# Best Case: O(1) – The target is the middle element in the first comparison.
# Worst Case: O(log n) – The search space is halved with each iteration, 
# so in the worst case, the algorithm performs logarithmic comparisons (base 2).


# Binary Search

def binary(lst,target):
    l=0
    u=len(lst)-1
    
    while l<=u:
        m=(l+u)//2

        if lst[m]==target:
            return m
        else:
            if lst[m]<target:
                l=m+1
            else:
                u=m-1
    return -1

res=binary([1,2,4,6,8,33,66,99],8)
if res==-1:
    print('Not found')
else:
    print(f'Found at {res} index')


# Find first Occurance

def first_occ(lst,target):
    l,r=0,len(lst)-1

    while l<=r:
        m=(l+r)//2

        if lst[m]==target:
            j=m
            r=m-1
            
        else:
            if lst[m]<target:
                r=m-1
            else:
                l=m+1
    return j

        
print(first_occ([1,2,2,2,2,3,4,5,6],2))

# Find Square Root

def sqrt(x):
    if x<2:
        return x
    l,r=2,x//2

    while l<=r:
        m=(l+r)//2
        sqr=m*m
        if sqr==x:
            return m
        else:
            if sqr<x:
                l=m+1
            else:
                r=m-1

    return r

print(sqrt(12))


# Binary Search Using Recursion

def rec_bin(lst,target,low,high):
    if low<=high:
        m=(low+high) // 2
        if lst[m]==target:
            return m
        elif lst[m]<target:
            return rec_bin(lst,target,m+1,high)
        else:
            return rec_bin(lst,target,low,m-1)
        
    else:
        return -1
    
ls=[1,2,3,4,5,6,8]

print(rec_bin(ls,3,0,len(ls)-1))