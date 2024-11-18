def heapify(arr,n,i):
    largest=i  #initializing largest as root
    left=2*i+1  # index of left
    right=2*i+2  #index of right 
#if left is greater than root/parent
    if left<n and arr[left]>arr[largest]:
        largest=left  
#if right is greater than root/parent
    if right<n and arr[right]>arr[largest]:
        largest=right
# if parent index change the swap and heapify
    if i!=largest:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)
def heap_sort(arr):
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)

arr=[30,4,7,3,5,19]
heap_sort(arr)
# print(arr)
def heapify_min(arr,n,i):
    smallest=i
    left=2*i+1
    right=2*i+2
    if left<n and arr[left]<arr[smallest]:
        smallest=left
    if right<n and arr[right]<arr[smallest]:
        smallest=right
    if i != smallest:
        arr[i],arr[smallest]=arr[smallest],arr[i]
        heapify_min(arr,n,smallest)
def heap_sorts(arr):
    n=len(arr)

    for i in range(n//2-1,-1,-1):
        heapify_min(arr,n,i)

    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify_min(arr,i,0)

arr=[3,19,1,14,8,7]
heap_sorts(arr)
print(arr)


def heapify2(arr,n,i):
    largest=i
    left=2*i+1
    right=2*i+2

    if left <n and arr[left]>arr[largest]:
        largest=left
    if right<n and arr[right]> arr[largest]:
        largest=right
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify2(arr,n,largest)

def heapsort2(arr):
    n=len(arr)

    for i in range(n//2,-1,-1):
        heapify(arr,n,i)

    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify2(arr,i,0)



    
def heapify3(arr,n,i):
    smallest=i
    left=2*i+1
    right=2*i+2
    if left<n and arr[left]<arr[smallest]:
        smallest=left
    if right<n and arr[right]<arr[smallest]:
        smallest=right
    if smallest!=i:
        arr[i],arr[smallest]=arr[smallest],arr[i]
        heapify3(arr,n,smallest)
def heap_sort3(arr):
    n=len(arr)
    arr1=[]
    for i in range(n//2-1,-1,-1):
        heapify3(arr,n,i)
    while arr:
        arr1.append(arr.pop(0))
        heapify3(arr,len(arr),0)
    return arr1   
arr=[3,5,3,1,4,5,6,8,5,3,21,1,4,7]
# print(heap_sort3(arr))


# print(arr)
def heapifies(arr,n,i):
    large=i
    left=2*i+1
    right=2*i+2

    if left<n and arr[left]>arr[large]:
        large=left
    if right<n and arr[right]>arr[large]:
        large=right
    if large!=i:
        arr[large],arr[i]=arr[i],arr[large]
        heapifies(arr,n,large)
def heapsorts(arr):
    n=len(arr)

    for i in range(n//2-1,-1,-1):
        heapifies(arr,n,i)

    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapifies(arr,i,0)


def heapifys(arr,n,i):
    large=i
    left=2*i+1
    right=2*i+2

    if left<n and arr[left]>arr[large]:
        large=left
    if right<n and arr[right]>arr[large]:
        large=right
    if large!=i:
        arr[i],arr[large]=arr[large],arr[i]
        heapifys(arr,n,large)

def heapsort(arr):
    n=len(arr)

    for i in range(n//2-1,-1,-1):
        heapifys(arr,n,i)

    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapifys(arr,i,0)
        
