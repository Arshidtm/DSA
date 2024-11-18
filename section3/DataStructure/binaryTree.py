class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self) -> None:
        self.root=None

    def add(self,data):
        if not self.root:
            self.root=Node(data)
            return
        self.recursiveAdd(data,self.root)
        
    def recursiveAdd(self,data,node):
        if not node.left:
            node.left=Node(data)
        elif not node.right:
            node.right=Node(data)
        else:
            self.recursiveAdd(data,node.left)

    def remove(self,data):
        if not self.root:
            return
        if self.root.data==data:
            self.root=None
            return
        parent=self.removeParent(data,self.root)
        if parent:
            if parent.left.data==data:
                parent.left=None
                return
            if parent.right.data==data:
                parent.right=None
                return
        print("no such value")
            
        
    def removeParent(self,data,node):
        if node.left.data==data:
            return node
        if node.right.data==data:
            return node
        
        if node.left:
            parent=self.removeParent(data,node.left)
            if parent:
                return parent
        
        if node.right:
            parent=self.removeParent(data,node.right)
            if parent:
                return parent

        return None     


    def display(self,depth=0,node=None):
        if not node:
            node=self.root

        print(" "*depth,node.data)
        if node.left:
            self.display(depth+1,node.left)
        if node.right:
            self.display(depth+1,node.right)

biTree=BinaryTree()
biTree.add(10)
biTree.add(11)
biTree.add(12)
biTree.add(21)
biTree.add(22)
biTree.add(31)
# biTree.display()
# # biTree.remove(21)
# biTree.display()


class BNode:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None

class Binary:
    def __init__(self) -> None:
        self.root=None

    def add(self,data):
        
        if not self.root:
            self.root=BNode(data)
            return
        self.recursiveAdd(data,self.root)
        
    def recursiveAdd(self,data,node):
        if not node.left:
            node.left=BNode(data)
        elif not node.right:
            node.right=BNode(data)
        else:
            self.recursiveAdd(data,node.left)
        
    def display(self,depth=0,node=None):
        if not node:
            node=self.root
        if not node:
            return
        print(' '*depth,node.data)
        if node.left:
            self.display(depth+1,node.left)
        if node.right:
            self.display(depth+1,node.right)

    def remove(self,data):
        if not self.root:
            return
        if self.root.data==data:
            self.root=None
            return
        parent=self.recursiveRemove(data,self.root)
        if parent:
            if parent.left.data==data:
                parent.left=None
            elif parent.right.data==data:
                parent.right=None
            return
        print("No such value")

    def recursiveRemove(self,data,node):
        if node.left.data==data:
            return node
        elif node.right.data==data:
            return node

        if node.left:
            found=self.recursiveRemove(data,node.left)
            if found:
                return found
        if node.right:
            found=self.recursiveRemove(data,node.right)
            if found:
                return found
        return None

        
        


# bi=Binary()
# bi.add(10)
# bi.add(12)
# bi.add(17)
# bi.add(112)
# bi.display()



class BSTNode:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root=None

    def add(self,data):
        if not self.root:
            self.root=BSTNode(data)
            return
        self.recursiveAdd(data,self.root)
        
    def recursiveAdd(self,data,node):
        if data<node.data:
            if not node.left:
                node.left=BSTNode(data)
            else:
                self.recursiveAdd(data,node.left)
        elif data>node.data:
            if not node.right:
                node.right=BSTNode(data)
            else:
                self.recursiveAdd(data,node.right)

    def diaplay(self):
        result=[]
        if not self.root:
            return None
        # self.inOrdertraversal(self.root,result)
        # self.preOrderTraversal(self.root,result)
        self.postOrderTraversal(self.root,result)
        print(result)
        
    def inOrdertraversal(self,node,result):
        if not node:
            return None
        else:
            self.inOrdertraversal(node.left,result)
            result.append(node.data)
            self.inOrdertraversal(node.right,result)

    def preOrderTraversal(self,node,result):
        if not node:
            return None
        else:
            result.append(node.data)
            self.preOrderTraversal(node.left,result)
            self.preOrderTraversal(node.right,result)

    def postOrderTraversal(self,node,result):
        if not node:
            return None
        else:
            self.postOrderTraversal(node.left,result)
            self.postOrderTraversal(node.right,result)
            result.append(node.data)


    def search(self,data):
        if not self.root:
            return False
        if self.root.data==data:
            return True
        return self.recursiveSearch(data,self.root)
    
    def recursiveSearch(self,data,node):
        if not node:
            return False
        if node.data==data:
            return True
        if node.data>data:
            return self.recursiveSearch(data,node.left)
        else:
            return self.recursiveSearch(data,node.right)

    

        
    def delete(self,data):
        self.root=self._delete(self.root,data)

    def _delete(self,node,data):
        if not node:
            return node
        
        if data<node.data:
            node.left=self._delete(node.left,data)
        elif data>node.data:
            node.right=self._delete(node.right,data)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            node.data=self._minValue(node.right)
            node.right=self._delete(node.right,node.data)
        return node
    
    def _minValue(self,node):
        curr=node
        while curr.left:
            curr=curr.left

        return curr.data
    
def findClosestValue(tree,target):
    return _findClosestValue(tree.root,target,float('inf'))

def _findClosestValue(node,target,closest):
    if not node:
        return closest
    if abs(target-closest)>abs(target-node.data):
        closest=node.data
    if target<node.data:
        return _findClosestValue(node.left,target,closest)
    elif target>node.data:
        return _findClosestValue(node.right,target,closest)
    else:
        return closest

def isBST(root,minVal=float('-inf'),maxVal=float('inf')):
    if not root:
        return True
    if not(minVal<root.data<maxVal):
        return False
    return isBST(root.left,minVal,root.data) and isBST(root.right,root.data,maxVal)

    


BST=BinarySearchTree()
# BST.add(45)
# BST.add(23)
# # BST.add(44)
# BST.add(43)
# BST.add(14)
# BST.add(54)
# # BST.diaplay()
# # print(BST.search(44))
# # BST.delete(44)
# BST.diaplay()
# print(findClosestValue(BST,44))
# # print(isBST(BST.root))
        


class BNodes:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None

class BSTree:
    def __init__(self) -> None:
        self.root=None

    def insert(self,data):
        if not self.root:
            self.root=BNode(data)
            return
        self._insert(data,self.root)

    def _insert(self,data,node):
        if data<node.data:
            if not node.left:
                node.left=BNode(data)
            else:
                self._insert(data,node.left)
        elif data>node.data:
            if not node.right:
                node.right=BNode(data)
            else:
                self._insert(data,node.right)

    def display(self):
        result=[]
        if not self.root:
            return
        self.inOrderTraversal(self.root,result)
        print(result)
        
    def inOrderTraversal(self,node,result):
        if not node:
            return node
        else:
            self.inOrderTraversal(node.left,result)
            result.append(node.data)
            self.inOrderTraversal(node.right,result)

    def contain(self,data):
        if not self.root:
            return False
        return self._contain(data,self.root)
        
    def _contain(self,data,node):
        if node.data==data:
            return True
        if data<node.data:            
            return self._contain(data,node.left)
        else:
            return self._contain(data,node.right)
        
    def delete(self,data):
        self.root=self._delete(data,self.root)

    def _delete(self,data,node):
        if not node:
            return node
        if data<node.data:
            node.left=self._delete(data,node.left)
        elif data>node.data:
            node.right=self._delete(data,node.right)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            node.data=self._minVal(node.right)
            node.right=self._delete(node.data,node.right)
        return node

    def _minVal(self,node):
        curr=node
        while curr.left:
            curr=curr.left
        return curr.data

def findClosestValue1(tree,target):
    return _findClosestValue1(tree.root,target,float('inf'))

def _findClosestValue1(node,target,closest):
    if not node:
        return closest
    if abs(target-closest)>abs(target-node.data):
        closest=node.data

    if target<node.data:
        return _findClosestValue1(node.left,target,closest)
    elif target>node.data:
        return _findClosestValue1(node.right,target,closest)
    else:
        return closest  

def isValidBST(root,min_val=float('-inf'),max_val=float('inf')):
    if not root:
        return True
    if not (min_val<root.data<max_val):
        return False
    return isValidBST(root.left,min_val,root.data) and isValidBST(root.right,root.data,max_val)


# BTS=BSTree()
# BTS.insert(10)
# BTS.insert(18)
# BTS.insert(9)
# BTS.insert(17)
# BTS.insert(36)
# BTS.insert(63)
# BTS.display()
# # print(BTS.contain(90))
# BTS.delete(18)
# BTS.display()
# print(findClosestValue1(BTS,11))
# print(isValidBST(BTS.root))

def findclose(tree,target):
    return _findclose(tree.root,target,float('inf'))

def _findclose(node,target,close):
    if not node:
        return close
    if abs(target-close)>abs(target-node.data):
        close=node.data
    if target<node.data:
        return _findclose(node.left,target,close)
    elif target>node.data:
        return _findclose(node.right,target,close)
    else:
        return close

def isBSTree(root,min_val=float('-inf'),max_val=float('inf')):
    if not root:
        return True

    if not (min_val<root.data<max_val):
        return False
    return isBSTree(root.left,min_val,root.data) and isBSTree(root.right,root.data,max_val)


class BSTNode:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None

class Bst:
    def __init__(self) -> None:
        self.root=None

    def insert(self,data):
        if not self.root:
            self.root=BSTNode(data)
            return
        self._insert(data,self.root)


    def _insert(self,data,node):
        if data<node.data:
            if not node.left:
                node.left=BSTNode(data)
            else:
                self._insert(data,node.left)
        elif data>node.data:
            if not node.right:
                node.right=BSTNode(data)
            else:
                self._insert(data,node.right)


    def display(self):
        result=[]
        if not self.root:
            return
        self.inorderTraversal(self.root,result)


    def inorderTraversal(self,node,result):
        if not node:
            return node
        else:
            self.inorderTraversal(node.left,result)
            result.append(node.data)
            self.inorderTraversal(node.right,result)

    
    def contains(self,data):
        if not self.root:
            return False
        return self._contains(data,self.root)
        

    def _contains(self,data,node):
        if data==node.data:
            return True

        if data<node.data:
            return self._contains(data,node.data)
        elif data>node.data:
            return self._contains(data,node.right)

    def delete(self,data):
        self.root=self._delete(data,self.root)

    def _delete(self,data,node):
        if not node:
            return node

        if data<node.data:
            node.left=self._delete(data,node.left)
        elif data>node.data:
            node.right=self._delete(data,node.right)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            node.data=self._minVal(node.right)
            node.right=self._delete(node.data,node.right)

        return node

    def _minVal(self,node):
        curr=node
        while curr.left:
            curr=curr.left
        return curr.data



class BiNode:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None

class BiTree:
    def __init__(self) -> None:
        self.root=None

    def add(self,data):
        
        if not self.root:
            self.root=BiNode(data)
            return
        self._recursiveAdd(data,self.root)
        
    def _recursiveAdd(self,data,node):
        if not node.left:
            node.left=BiNode(data)
        elif not node.right:
            node.right=BiNode(data)
        else:
            self._recursiveAdd(data,node.left)

    def remove(self,data):
        if not self.root:
            return
        if self.root.data==data:
            self.root=None
            return
        parent=self._findParent(data,self.root)
        if parent:
            if parent.left.data==data:
                parent.left=None                
            else:
                parent.right=None
            return
        return None
            
        
    def _findParent(self,data,node):
        if node.left.data==data:
            return node
        if node.right.data==data:
            return node
        
        if node.left:
            found=self._findParent(data,node.left)
            if found:
                return found
        if node.right:
            found=self._findParent(data,node.right)
            if found:
                return found
        return None
    
    def display(self,depth=0,node=None):
        if not node:
            node=self.root
        if not node:
            return
        print(' '*depth,node.data)
        if node.left:
            self.display(depth+1,node.left)
        if node.right:
            self.display(depth+1,node.right)


class BSTNODE:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None

class BSTREEs4:
    def __init__(self) -> None:
        self.root=None

    def add(self,data):
        if not self.root:
            self.root=BSTNODE(data)
            return
        self._add(data,self.root)
        
    def _add(self,data,node):
        if data<node.data:
            if not node.left:
                node.left=BSTNODE(data)
            else:
                self._add(data,node.left)
        elif data>node.data:
            if not node.right:
                node.right=BSTNODE(data)
            else:
                self._add(data,node.right)

    def display(self):
        result=[]
        if not self.root:
            return None
        
        self.inordertraversal(self.root,result)
        print(result)


    def inordertraversal(self,node,result):
        if not node:
            return node
        if node:
            self.inordertraversal(node.left,result)
            result.append(node.data)
            self.inordertraversal(node.right,result)

    def search(self,target):
        if not self.root:
            return False
        if self.root.data==target:
            return True
        return 
    
    def _search(self,target,node):
        if not node:
            return False
        if node.data==target:
            return True
        
        if target<node.data:
            return self._search(target,node.left)
        else:
            return self._search(target,node.right)
        

    def delete(self,data):
        self.root=self._delete(data,self.root)

    def _delete(self,data,node):
        if not node:
            return node
        if data<node.data:
            node.left=self._delete(data,node.left)
        elif data>node.data:
            node.right=self._delete(data,node.right)
        else:
            if not node.left:
                return node.right
            
            if not node.right:
                return node.left
            
            node.data=self._minValue(node.right)
            node.right=self._delete(node.data,node.right)
        return node

    def _minValue(self,node):
        curr=node
        while curr.left:
            curr=curr.left

        return curr.data
    
def findClosest(node,data,closest=float('inf')):
    if not node:
        return closest
    if abs(data-closest)>abs(data-node.data):
        closest=node.data

    if data<node.data:
        return findClosest(node.left,data,closest)
    elif data>node.data:
        return findClosest(node.right,data,closest)
    else:
        return closest
    

    
def isBST(root,min_val=float('-inf'),max_val=float('inf')):
    if not root:
        return True
    if not (min_val<root.data<max_val):
        return False
    return isBST(root.left,min_val,root.data) and isBST(root.right,root.data,max_val)

BST=BSTREEs4()
BST.add(45)
BST.add(23)
BST.add(44)
BST.add(43)
BST.add(14)
BST.add(54)

# BST.display()

# print(findClosest(BST.root,22))
    
def find_close(root,target,closest=float('inf')):
    if not root:
        return closest

    if abs(target-closest)  > abs(target-root.data):
        closest=root.data

    if target<root.data:
        return find_close(root.left,target,closest)
    elif target>root.data:
        return find_close(root.right,target,closest)
    else:
        return closest
    
def isBSTre(root,min_val=float('-inf'),max_val=float('inf')):
    if not root:
        return True
    if not (min_val<root.data<max_val):
        return False
    return isBSTre(root.left,min_val,root.data) and isBSTre(root.right,root.data,max_val)


class BINOD:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None

class BSTreEE:
    def __init__(self) -> None:
        self.root=None

    def add(self,data):
        if not self.root:
            self.root=BINOD(data)
            return
        self._add(data,self.root)
        
    def _add(self,data,node):
        if data<node.data:
            if not node.left:
                node.left=BINOD(data)
            else:
                self._add(data,node.left)
        elif data>node.data:
            if not node.right:
                node.right=BINOD(data)
            else:
                self._add(data,node.right)

    def search(self,data):
        if not self.root:
            return False
        return self._search(data,self.root)
    
    def _search(self,data,node):
        if not node:
            return False
        if node.data==data:
            return True
        if data<node.data:
            return self._search(data,node.left)
        if data>node.data:
            return self._search(data,node.right)
        

    

    def delete(self,data):
        self.root=self._delete(data,self.root)

    
    def _delete(self,data,node):
        if not node:
            return node
        if data<node.data:
            node.left=self._delete(data,node.left)
        elif data>node.data:
            node.right=self._delete(data,node.right)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            node.data=self.min_val(node.right)
            node.right=self._delete(node.data,node.right)

        return node
    


    def min_val(self,node):
        curr=node
        while curr.left:
            curr=curr.left
        return curr.data
    


    


    


# def findClose(root,data,closest=float('inf')):
#     if not root:
#         return closest
#     if abs(data-closest)> abs(data-root.data):
#         closest=root.data
#     if data<root.data:
#         return findClose(root.left,data,closest)
#     elif data>root.data:
#         return findClose(root.right,data,closest)
#     else:
#         return closest
    
# def ISBST(root,min_val=float('-inf'),max_val=float('inf')):
#     if not root:
#         return True
#     if not (min_val<root.data<max_val):
#         return False
#     return ISBST(root.left,min_val,root.data) and ISBST(root.right,root.data,max_val)

    def display(self):
        result=[]
        if not self.root:
            return
        self._inorderTraversal(self.root,result)
        print(result)    

    def _inorderTraversal(self,node,result):
        if node:
            self._inorderTraversal(node.left,result)
            result.append(node.data)
            self._inorderTraversal(node.right,result)

BST=BSTreEE()
BST.add(45)
BST.add(23)
BST.add(44)
BST.add(43)
BST.add(14)
BST.add(54)
BST.display()


# print(isBST(BST.root))





# 
# print(BST.search(5))

class BN:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None

class B:
    def __init__(self) -> None:
        self.root=None

    def add(self,data):
        if not self.root:
            self.root=BN(data)
            return
        self._add(data,self.root)

    def _add(self,data,node):
        if data<node.data:
            if not node.left:
                node.left=BN(data)
            else:
                self._add(data,node.left)
        if data>node.data:
            if not node.right:
                node.right=BN(data)
            else:
                self._add(data,node.right)

    def delete(self,data):
        self.root=self._delete(data,self.root)

    def _delete(self,data,node):
        if not node:
            return node
        if data<node.data:
            node.left=self._delete(data,node.left)
        elif data>node.data:
            node.right=self._delete(data,node.right)
        else:
            if not node.right:
                return node.left
            if not node.left:
                return node.right
            
            node.data=self._minVal(node.right)
            node.right=self._delete(node.data,node.right)

    def _minVal(self,node):
        curr=node
        while curr.left:
            curr=curr.left
        return curr.data
    
def findClosestof(root,target,closest=float('inf')):
    if not root:
        return closest
    if abs(target-closest)>abs(target-root.data):
        closest=root.data
    if target<root.data:
        return findClosestof(root.left,target,closest)
    elif target>root.data:
        return findClosestof(root.right,target,closest)
    else:
        return closest

def isBst(root,min_va=float('-inf'),max_val=float('inf')):
    if not root:
        return True
    if not (min_va<root.data<max_val):
        return False
    return isBst(root.left,min_va,root.data) and isBst(root.right,root.data,max_val)