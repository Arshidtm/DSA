class HeapNode:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None

class MinHeap:
    def __init__(self) -> None:
        self.root=None

    
    def insert(self,data):
        if not self.root:
            self.root=HeapNode(data)
            return
        self._insert(data,self.root)
        
    def _insert(self,data,node):
        if not node.left:
            node.left=HeapNode(data)
            self.heapify_up(node.left)
        elif not node.right:
            node.right=HeapNode(data)
            self.heapify_up(node.right)
        else:
            if self._getCount(node.left)<= self._getCount(node.right):
                self._insert(data,node.left)
            else:
                self._insert(data,node.right)

    def _getCount(self,node):
        if not node:
            return 0
        
        return 1+self._getCount(node.left)+self._getCount(node.right)
    
    def heapify_up(self,node):
        while node and node!=self.root:
            parent=self._parentNode(node,self.root)
            if parent.data>node.data:
                parent.data,node.data=node.data,parent.data
                node=parent
            else:
                break

    def _parentNode(self,node,root):
        if root.left==node or root.right==node:
            return root
        
        if root.left:
            parent=self._parentNode(node,root.left)
            if parent:
                return parent
        if root.right:
            parent=self._parentNode(node,root.right)
            if parent:
                return parent
        return None

    def extract(self):
        if not self.root:
            return
        min=self.root.data
        lastNode=self._removeLastNode()
        if lastNode:
            self.root.data=lastNode
            self.heapify_down(self.root)
        else:
            self.root=None
        return min
    
    def _removeLastNode(self):
        queue=[self.root]
        lastnode=None
        while len(queue)!=0:
            curr=queue.pop(0)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            if not curr.left and not curr.right:
                lastnode=curr
        if lastnode:
            parent=self._parentNode(lastnode,self.root)
            
            if parent.left==lastnode:
                parent.left=None
            else:
                parent.right=None
            return lastnode.data
        return None
    
    def heapify_down(self,node):
        while node:
            small=node
            if node.left and node.left.data<small.data:
                small=node.left
            if node.right and node.right<small.data:
                small=node.right
            
            if small!=node:
                small.data,node.data=node.data,small.data
                node=small
            else:
                break


            
class MaxHeap:
    def __init__(self) -> None:
        
        self.root=None

    def insert(self,data):
        if not self.root:
            self.root=HeapNode(data)
            return
        self._insert(data,self.root)

    def _insert(self,data,node):
        
        if not node.left:
            node.left=HeapNode(data)
            self.heapify_up(node.left)
        elif not node.right:
            node.right=HeapNode(data)
            self.heapify_up(node.right)
        else:
            if self._getcount(node.left)<=self._getcount(node.right):
                self._insert(data,node.left)
            else:
                self._insert(node.right)


    
    def _getcount(self,node):
        if not node:
            return 0
        return 1+self._getcount(node.left)+self._getcount(node.right)
    
    def heapify_up(self,node):
        while node and node!=self.root:
            parent=self._parentNode(node,self.root)
            if parent.data<node.data:
                parent.data,node.data=node.data,parent.data
                node=parent
            else:
                break



    def _parentNode(self,node,root):
        if root.left==node or root.right==node:
            return root
        if root.left:
            parent=self._parentNode(node,root.left)
            if parent:
                return parent
        if root.right:
            parent=self._parentNode(node,root.right)
            if parent:
                return parent
        return None
    
    def extract(self):
        if not self.root:
            return None
        max=self.root.data
        lastNode=self._removeLastNode()
        if lastNode:
            self.root.data=lastNode.data
            self.heapify_down(self.root)
        else:
            self.root=None
        return max
    


    def _removeLastNode(self):
        queue=[self.root]
        lastnode=None
        while len(queue)!=0:
            curr=queue.pop(0)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            if not curr.left and not curr.right:
                lastnode=curr
        if lastnode:
            parent=self._parentNode(lastnode,self.root)
            if parent.left==lastnode:
                parent.left=None
            else:
                parent.right=None
            return lastnode
        return None
    
    def heapify_down(self,node):
        while node:
            large=node
            if node.left and node.left.data>large.data:
                large=node.left
            if node.right and node.right.data>large.data:
                large=node.right
            if large!=node:
                node.data,large.data=large.data,node.data
                node=large
            else:
                break




class HeapNode2:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None

class Min:
    def __init__(self) -> None:
        self.root=None

    def insert(self,data):
        if not self.root:
            self.root=HeapNode2(data)
            return
        self._insert(data,self.root)

    def _insert(self,data,node):
        if not node.left:
            node.left=HeapNode2(data)
            self.heapify_up(node.left)
        elif not node.right:
            node.right=HeapNode2(data)
            self.heapify_up(node.right)
        else:
            if self._getCount(node.left)<=self._getCount(node.right):
                self._insert(data,node.left)
            else:
                self._insert(data,node.right)

    def _getCount(self,node):
        if not node:
            return 0
        return 1+ self._getCount(node.left)+self._getCount(node.right)
    


    def heapify_up(self,node):
        while node and node!=self.root:
            parent=self.parentNode(node,self.root)
            if parent.data>node.data:
                parent.data,node.data=node.data,parent.data

                node=parent
            else:
                break


    def parentNode(self,node,root):
        if root.left.data==node.data:
            return root
        if root.right.data==node.data:
            return root
        if root.left:
            parent=self.parentNode(node,root.left)
            if parent:
                return parent
        if root.right:
            parent=self.parentNode(node,root.right)
            if parent:
                return parent
        return None


    def extract(self):
        if not self.root:
            return
        min_val=self.root.data
        lastNode=self._extractLast()
        if lastNode:
            self.root.data=lastNode.data
            self.heapify_down(self.root)
        else:
            self.root=None
        return min_val
    
    def _extractLast(self):
        queue=[self.root]
        lastnode=None

        while queue:
            curr=queue.pop(0)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            if not curr.left and not curr.right:
                lastnode=curr
        if lastnode:
            parent=self.parentNode(lastnode,self.root)
            if parent.left==lastnode:
                parent.left=None
            elif parent.right==lastnode:
                parent.right=None
            return lastnode
        return None




    def heapify_down(self,node):
        
        while node:
            small=node
            if node.left and node.left.data<small.data:
                small=node.left
            if node.rigt and node.right.data<small.data:
                small.node.right
            if small!=node:
                small.data,node.data=node.data,small.data
                node=small
            else:
                break
            


class HeapqNode:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None

    
class MinHeapq:
    def __init__(self) -> None:
        self.root=None


    def add(self,data):
        if not self.root:
            self.root=HeapqNode(data)
            return
        self._add(data,self.root)
        
    def _add(self,data,node):
        if not node.left:
            node.left=HeapqNode(data)
            self.heapify_up(node.left)
        elif not node.right:
            node.right=HeapqNode(data)
            self.heapify_up(node.right)
        else:
            if self._getCount(node.left)<=self._getCount(node.right):
                self._add(data,node.left)
            else:
                self._add(data,node.right)
        

    def _getCount(self,node):
        if not node:
            return 0
        return 1+self._getCount(node.left)+self._getCount(node.right)

    def heapify_up(self,node):
        while node and node!=self.root:
            parent=self.parentNode(node,self.root)
            if parent.data>node.data:
                parent.data,node.data=node.data,parent.data
                node=parent
            else:
                break

    def parentNode(self,node,root):
        if root.left.data==node.data:
            return root
        if root.right.data==node.data:
            return root
        if root.left:
            parent=self.parentNode(node,root.left)
            if parent:
                return parent
        if root.right:
            parent=self.parentNode(node,root.right)
            if parent:
                return parent
        return None
    
    def extract(self):
        if not self.root:
            return
        min_val=self.root.data
        lastNode=self.removeLastnode()
        if lastNode:
            self.root.data=lastNode.data
            self.heapify_down(self.root)
        else:
            self.root=None
        return min_val


    def removeLastnode(self):
        queue=[self.root]
        lastnode=None
        while queue:
            node=queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if not node.left and not node.right:
                lastnode=node
        if lastnode:
            parent=self.parentNode(lastnode,self.root)
            if parent.left.data==lastnode.data:
                parent.left=None
                return
            if parent.right.data==lastnode:
                parent.right=None
            return lastnode
        return None
        


    def heapify_down(self,node):
        while node:
            small=node
            if node.left and node.left.data<small.data:
                small=node.left
            if node.right and node.right.data<small.data:
                small=node.right
            if node!=small:
                node.data,small.data=small.data,node.data
                node=small
            else:
                break


class HNode:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None
class MAX:
    def __init__(self) -> None:
        self.root=None
    def insert(self,data):
        if not self.root:
            self.root=HNode(data)
            return
        self._insert(data,self.root)
    def _insert(self,data,node):
        if not node.left:
            node.left=HNode(data)
            self.heapify_up(node.left)
        elif not node.right:
            node.right=HNode(data)
            self.heapify_up(node.right)
        else:
            if self._getCount(node.left)<= self._getCount(node.right):
                self._insert(data,node.left)
            else:
                self._insert(data,node.right)

    def _getCount(self,node):
        if not node:
            return 0
        return 1+self._getCount(node.left)+self._getCount(node.right) 
    def heapify_up(self,node):
        while node and node!=self.root:
            parent=self._parent(node,self.root)
            if parent.data<node.data:
                parent.data,node.data=node.data,parent.data
                node=parent
            else:
                break
   
    
    def display(self):
        result=[]
        if not self.root:
            return
        self.preorder(self.root,result)
        print(result)

    def preorder(self,node,result):
        if node:
            result.append(node.data)
            self.preorder(node.left,result)
            self.preorder(node.right,result)

    def extract(self):
        if not self.root:
            return
        min_val=self.root.data
        last=self._removeLastNOde()
        if last:
            self.root.data=last.data
        else:
            self.root=None
        return min_val
    def _removeLastNOde(self):
        queue=[self.root]
        last=None

        while queue:
            curr=queue.pop(0)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            if not curr.left and not curr.right:
                last=curr
        if last:
            parent=self._parent(last,self.root)
            if parent.left.data==last.data:
                parent.left=None
            else:
                parent.right=None
            return last
        return None
    def heapify_down(self,node):
        while node:
            large=node
            if node.left and node.left.data>large.data:
                large=node.left
            if node.right and node.right.data>large.data:
                large=node.right
            if large!=node:
                large.data,node.data=node.data,large.data
                node=large
            else:
                break
    def _parent(self,node,root):
        if root.left==node or root.right==node:
            return root
        if root.left:
            parent=self._parent(node,root.left)
            if parent:
                return parent
        if root.right:
            parent=self._parent(node,root.right)
            if parent:
                return parent
        return None
            

            
        
    

# max_heap=MAX()
# max_heap.insert(12)
# max_heap.insert(13)
# max_heap.insert(22)
# max_heap.insert(11)
# max_heap.insert(10)
# max_heap.insert(15)
# max_heap.insert(23)
# max_heap.insert(43)
# max_heap.display()

class HN:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None

class MinH:
    def __init__(self) -> None:
        self.root=None

    def insert(self,data):
        if not self.root:
            self.root=HN(data)
            return
        self._insert(data,self.root)
    def _insert(self,data,node):
        if not node.left:
            node.left=HN(data)
            self.heapify_up(node.left)
        elif not node.right:
            node.right=HN(data)
            self.heapify_up(node.right)
        else:
            if self.getCount(node.left)<=self.getCount(node.right):
                self._insert(data,node.left)
            else:
                self._insert(data,node.right)

    def getCount(self,node):
        if not node:
            return 0
        return 1+self.getCount(node.left)+self.getCount(node.right)
    
    def heapify_up(self,node):
        while node and node!=self.root:
            parent=self.parentNode(node,self.root)
            if parent.data>node.data:
                parent.data,node.data=node.data,parent.data
                node=parent
            else:
                break
             

        
    def parentNode(self,node,root):
        if node.data==root.left.data or node.data==root.right:
            return root
        if  root.left:
            found=self.parentNode(node,root.left)
            if found:
                return found
        elif root.right:
            found=self.parentNode(node,root.right)
            if found:
                return found
        return None
            

    def extract(self):
        if not self.root:
            return
        min_val=self.root.data
        last=self.removeLast()
        if last:
            self.root.data=last.data
            self.heapify_down(self.root)
        else:
            self.root=None
        return min_val

    def removeLast(self):
        queue=[self.root]
        lastNode=None
        while queue:
            curr=queue.pop(0)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            if not curr.left and not curr.right:
                lastNode=curr
        if lastNode:
            parent=self.parentNode(lastNode,self.root)
            if parent.left==lastNode.data:
                parent.left=None
            else:
                parent.right=None
            return lastNode
        return None
    def heapify_down(self,node):
        while node:
            small=node
            if node.left and node.left.data<node.data:
                small=node.left
            if node.right and node.right.data<node.data:
                small=node.right
            if small !=node:
                small.data,node.data=node.data,small.data
                node=small
            else:
                break

            

            

    


