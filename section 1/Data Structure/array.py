arr = [1, 2, 3, 4, 5]

# Accessing element at index 2 (O(1))
element = arr[2]  # O(1)

# Adding an element to the end of the list (O(1))
arr.append(3)  # O(1)

# Removing the last element from the list (O(1))
arr.pop()  # O(1)

# Adding an element to the start of the list (O(n))
arr.insert(0, 0)  # O(n)

# Removing the first element from the list (O(n))
arr.pop(0)  # O(n)

# Merging two lists (O(n))
arr2 = [6, 7, 8]
arr3 = arr + arr2  # O(n) for concatenation

# Removing two elements starting from index 1 (O(n))
arr3[1:3] = []  # O(n) for slicing and removal

# Multiplying all elements by two (O(n))
multiply_by_two = [x * 2 for x in arr3]  # O(n)

# Filtering even elements (O(n))
even = [x for x in arr3 if x % 2 == 0]  # O(n)

# Summing all elements in the list (O(n))
total_sum = sum(arr3)  # O(n)



# Remove Duplicates

def remove_dupli(lst):
    i=0
    while i <len(lst):
        j=i+1
        while j<len(lst):
            if lst[i]==lst[j]:
                lst.pop(i)
            else:
                j+=1
        i+=1
    return lst

print(remove_dupli([1,24,5,3,5,3,7,1,1,1,1,1,1,1]))

nums=[1,2,3,4,4,4,5,6]
print(remove_dupli(nums))
print(nums)


# Maximum Profit

def max_profit(prices):
    min_price=float('inf')
    max_prof=0

    for price in prices:
        if price<min_price:
            min_price=price
        elif price-min_price>max_prof:
            max_prof=price-min_price
    return max_prof

prices = [7,1,5,3,6,4]
print(max_profit(prices))


# Move Zero

def move_zero(nums):
    i=0
    for j in range(len(nums)):
        if nums[j]!=0:
            nums[i]=nums[j]
            i+=1
    for s in range(i,len(nums)):
        nums[s]=0

nums=[0,1,0,3,12]
move_zero(nums)
print(nums)






