class Graph:
    def __init__(self) -> None:
        self.graph={}

    def addVertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]

    def addEdge(self,vertex1,vertex2,isDirected=False):
        self.addVertex(vertex1)
        self.addVertex(vertex2)

        self.graph[vertex1].append(vertex2)
        if not isDirected:
            self.graph[vertex2].append(vertex1)

    def display(self):
        for key,value in self.graph.items():
            print(f"{key} => {value}")

    def getVertices(self):
        for key in self.graph:
            print(key)

    def getEdges(self):
        for key,values in self.graph.items():
            for value in values:
                print(f"({key},{value})")

    def removeVertex(self,vertex):
        if vertex in self.graph:
            del self.graph[vertex]
        for key,value in self.graph.items():
            if vertex in value:
                value.remove(vertex)

    def isEdge(self,vertex1,vertex2):
        return vertex1 in self.graph[vertex2] or vertex2 in self.graph[vertex2]
    

    def removeEdges(self,vertex1,vertex2):
        if self.isEdge(vertex1,vertex2):
            self.graph[vertex1].remove(vertex2)
            self.graph[vertex2].remove(vertex1)


    def DFStraversal(self,start,AlreadyVisited=set()):
        if start not in AlreadyVisited:
            AlreadyVisited.add(start)
            print(start,end=' ')

            for child in self.graph[start]:
                self.DFStraversal(child,AlreadyVisited)

    def BFStraversal(self,start):
        AlreadyVisited={start}
        queue=[start]

        while queue:
            curr=queue.pop(0)
            print(curr,end=' ')
            for child in self.graph[curr]:
                if child not in AlreadyVisited:
                    queue.append(child)
                    AlreadyVisited.add(child)

    def shortestPath(self,start,end):
        AlredyVisited={start}
        queue=[(start,[start])]

        while queue:
            curr,path=queue.pop(0)
            
            for child in self.graph[curr]:
                if child==end:
                    return path+[child]
                if child not in AlredyVisited:
                    queue.append((child,path+[child]))
                    AlredyVisited.add(child)
        return None
    

class Graph2:
    def __init__(self) -> None:
        self.graph={}

    def addVertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]

    def addEdge(self,vertex1,vertex2,isDirected=False):
        self.addVertex(vertex1)
        self.addVertex(vertex2)

        self.graph[vertex1].append(vertex2)
        if not isDirected:
            self.graph[vertex2].append(vertex1)

    def display(self):
        for key , value in self.graph.items():
            print(f"{key} => {value}")

    def removeVertex(self,vertex):
        if vertex in self.graph:
            del self.graph[vertex]

        for value in self.graph.values():
            if vertex in value:
                value.remove(vertex)


    def isEdge(self,vertex1,vertex2):
        return vertex1 in self.graph[vertex2] or vertex2 in self.graph[vertex1]
    
    def removeEdges(self,vertex1,vertex2):
        if self.isEdge(vertex1,vertex2):
            self.graph[vertex1].remove(vertex2)
            self.graph[vertex2].remove(vertex1)

    
    def DFStraversal(self,start,AlreadyVisited=set()):
        if start not in AlreadyVisited:
            AlreadyVisited.add(start)
            print(start,end=' ')
            for child in self.graph[start]:
                self.DFStraversal(child,AlreadyVisited)

        return AlreadyVisited
    
    def BFSTraversal(self,start):
        AlreadyVisited={start}
        queue=[start]

        while queue:
            curr=queue.pop(0)
            print(curr,end=' ')
            for child in self.graph[curr]:
                if child not in AlreadyVisited:
                    queue.append(child)
                    AlreadyVisited.add(child)

    def shortestPath(self,start,end):
        AlreadyVisit={start}
        queue=[(start,[start])]

        while queue:
            curr,path=queue.pop(0)

            for child in self.graph[curr]:
                if child==end:
                    return path+[child]
                if child not in AlreadyVisit:
                    queue.append((child,path+[child]))
                    AlreadyVisit.add(child)
        return None
    







graph=Graph2()
graph.addEdge('A','B')
graph.addEdge('B','C')
graph.addEdge('B','D')
graph.addEdge('D','C')
# graph.DFStraversal('A')
# graph.BFSTraversal('A')

# print(graph.shortestPath('A','C'))
# graph.display()  
# graph.getVertices()
# graph.getEdges() 
# graph.DFStraversal('A') 
# 

class Graph3:
    def __init__(self) -> None:
        self.graph={}

    def addVertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]

    def addEdge(self,vertex1,vertex2,isDirected=False):
        self.addVertex(vertex1)
        self.addVertex(vertex2)

        self.graph[vertex1].append(vertex2)
        if not isDirected:
            self.graph[vertex2].append(vertex1)

    def display(self):
        for key,value in self.graph.items():
            print(f"{key} => {value}")

    def removeVertex(self,vertex):
        if vertex in self.graph:
            del self.graph[vertex]

        for values in self.graph.values():
            if vertex in values:
                values.remove(vertex)

    
    
    def removeEdges(self,vert1,vert2):
        if vert2 in self.graph[vert1]:
            self.graph[vert1].remove(vert2)
            
        if vert1 in self.graph[vert2]:
            self.graph[vert2].remove(vert1)

    def DFStraversal(self,start,AlreadyVisited=set()):
        if start not in AlreadyVisited:
            AlreadyVisited.add(start)
            print(start,end=' ')

            for child in self.graph[start]:
                self.DFStraversal(child,AlreadyVisited)

    def BFSTraversal(self,start):
        AlreadyVisited={start}
        queue=[start]
        while queue:
            curr=queue.pop(0)
            for child in self.graph[curr]:
                if child not in AlreadyVisited:
                    queue.append(child)
                    AlreadyVisited.add(child)

    def shortestPath(self,start,end):
        AlreadyVisited={start}
        queue=[(start,[start])]

        while queue:
            curr,path=queue.pop(0)
            for  child in self.graph[curr]:
                if child==end:
                    return path+[child]
                if child not in AlreadyVisited:
                    queue.append((child,path+[child]))
                    AlreadyVisited.add(child)

                
        


gr=Graph3()
gr.addEdge('A','B')
gr.addEdge('A','C')
gr.addEdge('B','C')
gr.addEdge('B','D')
gr.addEdge('D','C')
# gr.removeEdges('A','C')
# gr.removeVertex('D')
# gr.display()
# gr.DFStraversal('A')

class AdjacencyMatrix:
    def __init__(self,vertices) -> None:
        self.vertices=vertices
        self.adj_matrix=[[0 for _ in range(vertices)] for _ in range(vertices)]

    def addEdges(self,v1,v2,weight=1):
        self.adj_matrix[v1][v2]=weight
        self.adj_matrix[v2][v1]=weight

    def removeEdge(self,v1,v2):

        self.adj_matrix[v1][v2]=0
        self.adj_matrix[v2][v1]=0

    def dispaly(self):
        for row in self.adj_matrix:
            print(row)

            
class GRaph:
    def __init__(self) -> None:
        self.graph={}

    def addVertex(self,v):
        if v not in self.graph:
            self.graph[v]=[]

    def addEdge(self,v1,v2,isD=False):
        self.addVertex(v1)
        self.addVertex(v2)
        self.graph[v1].append(v2)
        if isD:
            self.graph[v2].append(v1)

    
    def display(self):
        for key,value in self.graph.items():
            print(f"{key}=>{value}")

    def removeVertex(self,v):
        if v in self.graph:
            del self.graph[v]
        for value in self.graph.values():
            if v in value:
                value.remove(v)

    
    def removeEdge(self,v1,v2):
        if v1 in self.graph[v2]:
            self.graph[v2].remove(v1)
        if v2 in self.graph[v1]:
            self.graph[v1].remove(v2)

    def Dfs(self,start,AlreadyVisited=set()):
        if start not in AlreadyVisited:
            AlreadyVisited.add(start)
            print(start,end=' ')

            for child in self.graph[start]:
                self.Dfs(child,AlreadyVisited)


    def BFs(self,start):
        AlreadyVisited={start}
        queue=[start]

        while queue:
            curr=queue.pop(0)

            for child in self.graph[curr]:
                if child not in AlreadyVisited:
                    queue.append(child)
                    AlreadyVisited.add(child)

    
    def shortPath(self,start,end):
        AlreadyVisit={start}
        queue=[(start,[start])]

        while queue:
            curr,path=queue.pop(0)

            for child in self.graph[curr]:
                if child==end:
                    return path+[child]
                if child not in AlreadyVisit:
                    queue.append((child,path+[child]))
                    AlreadyVisit.add(child)
        return None


    def DFDS(self,start,alredy=set()):
        if start not in alredy:
            alredy.add(start)

            for child in self.graph[start]:
                self.DFDS(child,alredy)


                
    
class GR:
    def __init__(self) -> None:
        self.graph={}

    def addVertex(self,v):
        if v not in self.graph:
            self.graph[v]=[]
    
    def addEdges(self,v1,v2,isD=False):
        self.addVertex(v1)
        self.addVertex(v2)

        self.graph[v1].append(v2)
        if not isD:
            self.graph[v2].append(v1)


    def display(self):
        for key,values in self.graph.items():
            print(f"{key}=>{values}")

    def removeVertex(self,v):
        if v in self.graph:
            del self.graph[v]
        
        for values in self.graph.values():
            if v in values:
                values.remove(v)

    def removeedges(self,v1,v2):
        if not self.isEdge(v1,v2):
            return
        if v1 in self.graph[v2]:
            self.graph[v2].remove(v1)
        if v2 in self.graph[v1]:
            self.graph[v1].remove(v2)


    def isEdge(self,v1,v2):
        return v1 in self.graph[v2] or v2 in self.graph[v1]

    def DFs(self,start,AlreadyVisited=set()):
        if start not in AlreadyVisited:
            AlreadyVisited.add(start)

            print(start,end=' ')

            for child in self.graph[start]:
                self.DFs(child,AlreadyVisited)

    def Bfs(self,start):
        queue=[start]
        already={start}

        while queue:
            curr=queue.pop(0)
            print(curr,end=' ')
            for child in self.graph[curr]:
                if child not in already:
                    queue.append(child)
                    already.add(child)

    def short(self,start,end):
        alredy={start}

        queue=[(start,[start])]

        while queue:
            curr,path=queue.pop(0)
            for child in self.graph[curr]:
                if child == end:
                    return path+[child]
                if child not in alredy:
                    alredy.add(child)
                    queue.append((child,path+[child]))



