class TreeNode:
    def __init__(self,value) -> None:
        self.value=value
        self.children=[]

class Tree:
    
    def __init__(self) -> None:
        self.root=None


    def add(self,value,parentData=None):
        node=TreeNode(value)
        if not self.root:
            self.root=node
            return
        ParentNode=self.findNode(parentData,self.root)

        if not ParentNode:
            print('Parent not found')
            return
        ParentNode.children.append(node)
    def findNode(self,value,node):
        if node.value==value:
            return node        
        for child in node.children:
            foundNode=self.findNode(value,child)
            if foundNode:
                return foundNode            
        return None    
    def display(self,depth=0,node=None):
        if not node:
            node=self.root
        print(''*depth,node.value)
        for child in node.children:
            self.display(depth+1,child)
    
tr=Tree()
tr.add(10)
# tr.add(12,10)
# tr.display()

















class TrNode:
    def __init__(self,value) -> None:
        self.value=value
        self.children=[]

class Tr:
    def __init__(self) -> None:
        self.root=None
        

    def add(self,value,parentNode=None):
        node=TrNode(value)

        if not self.root:
            self.root=node
            return
        
        parent=self.findNode(parentNode,self.root)

        if not parent:
            print("parent not found")
            return
        parent.children.append(node)

    
    def findNode(self,value,node):
        if node.value==value:
            return node
        
        for child in node.children:
            foundNode=self.findNode(value,child)

            if foundNode:
                return foundNode
        
        return None
    
    def remove(self,value):
        if not self.root:
            print("Tree is empty")
            return
        if self.root.value==value:
            self.root=None
            return
        parent=self.findParent(value,self.root)
        if parent:
            for child in parent.children:
                if child.value==value:
                    parent.children.remove(child)
        print("not found value")   

    def findParent(self,value,node):
        for child in node.children:
            if value==child.value:
                return node
            foundParent=self.findParent(value,child)
            if foundParent:
                return foundParent
        return None
    
    def display(self,depth=0,node=None):
        if not node:
            node=self.root

        print(' '*depth,node.value)
        for child in node.children:
            self.display(depth+1,node=child)

# dt=Tr()
# dt.add(1)
# dt.add(2,1)
# dt.add(3,1)
# dt.add('a',1)
# dt.add(4,2)
# dt.add(5,2)
# dt.add(10,4)
# dt.add(11,4)
# dt.add(20,5)
# dt.add(21,5)
# dt.remove(21)
# dt.add(6,3)
# dt.add(7,3)
# dt.display()

class TreesNodes:
    def __init__(self,data) -> None:
        self.data=data
        self.children=[]

class Trees:
    def __init__(self) -> None:
        self.root=None

    def add(self,data,parentNode=None):
        node=TreesNodes(data)
        if not self.root:
            self.root=node
            return
        parent=self.findNode(parentNode,self.root)
        if not parent:
            print("node not found")
            return
        parent.children.append(node)



    def findNode(self,data,node):
        if node.data==data:
            return node
        for child in node.children:
            found=self.findNode(data,child)
            if found:
                return found
        return None
    
    def remove(self,data):
        if not self.root:
            print("empty tree")
            return 
        if data==self.root.data:
            self.root=None
            return
        parent=self.findParent(data,self.root)
        if parent:
            for child in parent.children:
                if child.data==data:
                    parent.children.remove(child)
                    return
        return "Not foound"
        

    def findParent(self,data,node):
        for child in node.children:
            if child.data==data:
                return node
            found=self.findParent(data,child)
            if found:
                return found
        return None
    
    def display(self,depth=0,node=None):
        if not node:
            node=self.root
        if not node:
            return
        print(" "*depth,node.data)
        for child in node.children:
            self.display(depth+1,child)

tre=Trees()
# tre.add(10)
# tre.add(20,10)
# tre.add(21,10)
# tre.add(32,20)
# tre.add(31,20)

# tre.display()
    

class TreNode:
    def __init__(self,data) -> None:
        self.data=data
        self.children=[]

class Tre:
    def __init__(self) -> None:
        self.root=None

    def add(self,data,parentNode=None):
        node=TreNode(data)
        if not self.root:
            self.root=node
            return
        parent=self.findNode(parentNode,self.root)
        if not parent:
            print("not such parent")
            return
        parent.children.append(node)


    def findNode(self,data,node):
        if node.data==data:
            return node
        for child in node.children:
            found=self.findNode(data,child)
            if found:
                return found
        return None
    
    def display(self,depth=0,node=None):
        if not node:
            node=self.root
        if not node:
            return
        print(' '*depth,node.data)
        for child in node.children:
            self.display(depth+1,child)

    def remove(self,data):
        if not self.root:
            return
        if self.root.data==data:
            self.root=None
        parent=self.findParent(data,self.root)

        if parent:
            for child in parent.children:
                if child.data==data:
                    parent.children.remove(child)
                    return
        print("NOt such value")
        return
    


    def findParent(self,data,node):
        for child in node.children:
            if child.data==data:
                return node
            found=self.findParent(data,child)
            if found:
                return found
        return None
    


tr=Tre()
# tr.add(10)
# tr.add(20,10)
# tr.add(30,10)
# tr.add(200,20)
# tr.add(250,20)
# tr.add(300,30)
# tr.display()
# print('/n/n')
# tr.remove(250)
# tr.display()

        
class TrNode:
    def __init__(self,data) -> None:
        self.data=data
        self.children=[]

class Tre:
    def __init__(self) -> None:
        self.root=None

    def add(self,data,parent=None):
        node=TrNode(data)
        if not self.root:
            self.root=node
            return
        parent=self.findNode(parent,self.root)
        if not parent:
            print("No such parent")
            return
        parent.children.append(node)

    def findNode(self,data,node):
        if node.data==data:
            return node
        for child in node.children:
            found=self.findNode(data,child)
            if found:
                return found
        return None
    
    def display(self,depth=0,node=None):
        if not node:
            node=self.root
        if not node:
            return
        print(' '*depth,node.data)
        for child in node.children:
            self.display(depth+1,child)

    def remove(self,data):
        if not self.root:
            return
        if self.root.data==data:
            self.root=None
        parent=self.findParent(data,self.root)
        if parent:
            for child in parent.children:
                if child.data==data:
                    parent.children.remove(child)
                    return
        print("no such value")
        

    def findParent(self,data,node):
        for child in node.children:
            if child.data==data:
                return node
            found=self.findParent(data,child)
            if found:
                return found
        return None
    



tr=Tre()
# tr.add(10)
# tr.add(21,10)
# tr.add(20,21)
# tr.add(13,10)
# # tr.remove(21)
# tr.display()

class Nodes:
    def __init__(self,data) -> None:
        self.data=data
        self.children=[]

class Treeee:
    def __init__(self) -> None:
        self.root=None


    def add(self,data,parent=None):
        node=Nodes(data)
        if not self.root:
            self.root=node
            return
        parent_node=self.findNode(parent,self.root)
        if not parent_node:
            print("no such parent")
        parent_node.children.append(node)

    def findNode(self,data,node):
        if node.data==data:
            return node
        for child in node.children:
            found=self.findNode(data,child)
            if found:
                return found
        return None
    
    def display(self,depth=0,node=None):
        if not node:
            node=self.root
        if not node:
            return node
        print(' '*depth,node.data)
        for child in node.children:
            self.display(depth+1,child)

    def remove(self,data):
        if not self.root:
            return None
        parent=self.findParent(data,self.root)
        if parent:
            for child in parent.children:
                if child.data==data:
                    parent.children.remove(child)
                    return
        print("no value found")

    def findParent(self,data,node):
        for child in node.children:
            if child.data==data:
                return node
            found=self.findParent(data,child)
            if found:
                return found
        return None

class TreeNode3:
    def __init__(self,data) -> None:
        self.data=data
        self.children=[]


class Tree3:
    def __init__(self) -> None:
        self.root=None

    def addNode(self,data,parent=None):
        node=TreeNode3(data)
        if not self.root:
            self.root=node
            return
        
        parentNode=self.foundNode(parent,self.root)
        if not parent:
            print("Parent not found")
            return
        parentNode.children.append(node)

        

    def foundNode(self,data,node):
        if node.data==data:
            return node
        for child in node.children:
            found=self.foundNode(data,child)
            if found:
                return found
        return None
    
    def display(self,depth=0,node=None):
        if not node:
            node=self.root

        if not node:
            return
        
        print(' '*depth,node.data)
        for child in node.children:
            self.display(depth+1,child)

    def removeNode(self,data):
        if not self.root:
            return
        if self.root.data==data:
            self.root=None
            return
        parent=self.findParent(data,self.root)
        if parent:
            for child in parent.children:
                if child.data==child:
                    parent.children.remove(child)
                    return
        print("No such value")



    def findParent(self,data,node):
        for child in node.children:
            if child.data==data:
                return node
            found=self.findParent(data,child)
            if found:
                return found
        return None
    
class TreNod:
    def __init__(self,data) -> None:
        self.data=data
        self.children=[]


class Tree4:
    def __init__(self) -> None:
        self.root=None

    def add(self,data,parent=None):
        node=TreNod(data)
        if not self.root:
            self.root=node
            return
        parentNode=self.foundNode(parent,self.root)
        if not parentNode:
            return None
        parentNode.children.append(node)


    def foundNode(self,data,node):
        if node.data==data:
            return node
        for child in node.children:
            found=self.foundNode(data,child)
            if found:
                return found
        return None
    
    

    def removeNode(self,data):
        if not self.root:
            return
        if self.root.data==data:
            self.root=None

        parent=self.findParent(data,self.root)
        if parent:
            for child in parent.children:
                if child.data==data:
                    parent.children.remove(child)
                    return
        return None

    def findParent(self,data,node):
        for child in node.children:
            if child.data==data:
                return node
            found=self.findParent(data,child)
            if found:
                return found
        return None
    
    def display(self,depth=0,node=None):
        if not node:
            node=self.root

        if not node:
            return node
        print(' '*depth,node.data)
        
        for child in node.children:
            self.display(depth+1,child)
    

tr=Tree4()
tr.add(10)
tr.add(20,10)
tr.add(25,10)
tr.add(30,20)
tr.add(35,20)
# tr.removeNode(20)
# tr.display() 


class TN:
    def __init__(self,data) -> None:
        self.data=data
        self.children=[]

class T:
    def __init__(self) -> None:
        self.root=None

    def add(self,data,parent=None):
        node=TN(data)
        if not self.root:
            self.root=node
            return
        parent=self.findNode(parent,self.root)
        if not parent:
            print("no such parent")
            return
        parent.children.append(node)
        

    def findNode(self,data,node):
        if node.data==data:
            return node
        for child in node.children:
            found=self.findNode(data,child)
            if found:
                return found
        return None
    
    def display(self,depth=0,node=None):
        if not node:
            node=self.root
        if not node:
            return
        print(" "*depth,node.data)
        for child in node.children:
            self.display(depth+1,child)

    def removeNOde(self,data):
        if not self.root:
            return
        if data==self.root.data:
            self.root=None
            return
        parent=self.findParent(data,self.root)
        if parent:
            for child in parent.children:
                if child.data==data:
                    parent.children.remove(child)
                    return
        return None



    def findParent(self,data,node):
        for child in node.children:
            if child.data==data:
                return node
            parent=self.findParent(data,child)
            if parent:
                return parent
        return None
    




        
    


