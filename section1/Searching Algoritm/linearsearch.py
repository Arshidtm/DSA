# Time Complexity:
# Best Case: O(1) – The target is the first element in the list.
# Worst Case: O(n) – The target is the last element or not present, requiring all elements to be checked.

# Linear Search
def linear_search(lst,target):
    for i in range(len(lst)):
        if target==lst[i]:
            return i
    return -1

result=linear_search([1,3,5,3,2,6,7,21],6)
if result==-1:
    print('Not found')
else:
    print(f'Found at {result} index')

# Linear Search On Sorted

def linear_search_sorted(lst,target):
    for i in range(len(lst)):
        if lst[i]>target:
            break
        elif target==lst[i]:
            return i
    return -1

result=linear_search([1,3,5,7,8,11,23,45],45)
if result==-1:
    print('Not found')
else:
    print(f'Found at {result} index')



# Linear Search on Linked List

class Node:
    def __init__(self,value) -> None:
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self) -> None:
        self.head=None

    def append(self,value):
        new_node=Node(value)
        if not self.head:
            self.head=new_node
        else: 
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=new_node

    def display(self):
        curr=self.head
        while curr:
            print(curr.value,end='->')
            curr=curr.next
        print(None)

    def linearsearch(self,target):
        if not self.head:            
            return -1
        curr=self.head
        curr_index=0
        if curr.value==target:
            return curr_index
        while curr and curr.value!=target:
            curr=curr.next
            curr_index+=1
        if not curr:
            return -1
        return curr_index
    

link=LinkedList()
link.append(11)
link.append(12)
link.append(13)
link.append(14)
link.append(15)
link.append(16)
link.display()
result=link.linearsearch(16)

if result==-1:
    print('Not found')
else:
    print(f'Found at {result} index')