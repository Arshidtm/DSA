class TrieNode:
    def __init__(self) -> None:
        self.children={}
        self.isEnd=False

class Trie:
    def __init__(self) -> None:
        self.root=TrieNode()

    def add(self,word):
        curr=self.root
        for char in word:
            if char not in curr.children:
                curr.children[char]=TrieNode()
            curr=curr.children[char]
        curr.isEnd=True

    def Search(self,word):
        curr=self.root
        for char in word:
            if char not in curr.children:
                return False
            curr=curr.children[char]
        if curr.isEnd:
            return True
        return False
    
    def remove(self,word):
        if not self.Search(word):
            print("No word found")
            return
        curr=self.root
        stack=[]
        for char in word:
            stack.append(curr)
            curr=curr.children[char]
        curr.isEnd=False

        while stack:
            node=stack.pop()
            char=word[len(stack)]

            if not node.children[char].isEnd and  not node.children[char].children:
                del node.children[char]
            else:
                break

        print("word removed")


class Trie2Node:
    def __init__(self) -> None:
        self.children={}
        self.isEnd=False

class Trie2:
    def __init__(self) -> None:
        self.root=Trie2Node()

    def add(self,word):
        curr=self.root
        for char in word:
            if char not in curr.children:
                curr.children[char]=Trie2Node()
            curr=curr.children[char]
        curr.isEnd=True

    def search(self,word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr=curr.children[char]
        if curr.isEnd:
            return True
        return False
    
    def remove(self,word):
        if not self.search(word):
            print("No such word ")
            return
        curr=self.root
        stack=[]

        for char in word:
            stack.append(char)
            curr=curr.children[char]
        curr.isEnd=False

        while stack:
            curr=stack.pop()
            char=word[len(stack)]

            if not curr.children[char].isEnd and not curr.children[char].children:
                del curr.children[char]
            else:
                break

    
    def remove2(self,word):
        if not self.search(word):
            print("Not such word")
            return 
        
        curr=self.root
        stack=[]

        for char in word:
            stack.append(curr)
            curr=curr.children[char]

        curr.isEnd=False

        while stack:
            node=stack.pop()
            char=word[len(stack)]

            if not node.children[char].isEnd and not node.children[char].children:
                del node.children[char]
            else:
                break 



class Trie3Node:
    def __init__(self) -> None:
        self.children={}
        self.isEnd=False


class Trie3:
    def __init__(self) -> None:
        self.root=Trie3Node()

    def add(self,word):
        curr=self.root
        for char in word:
            if char not in curr.children:
                curr.children[char]=Trie3Node()
            curr=curr.children[char]

        curr.isEnd=True



    def search(self,word):
        curr=self.root
        for char in word:
            if char not in curr.children:
                return False
            curr=curr.children[char]

        if curr.isEnd:
            return True
        return False




    
    def remove(self,word):
        if not self.search(word):
            print("No such word")
            return
        curr=self.root
        stack=[]

        for char in word:
            stack.append(curr)
            curr=curr.children[char]

        curr.isEnd=False

        while stack:
            node=stack.pop()
            char=word[len(stack)]

            if not node.children[char].isEnd and not node.children[char].children:
                del node.children[char]
            else:
                break
# trie=Trie3()
# trie.add('arun')
# trie.add('arjun')
# trie.remove('arun')
# print(trie.search('arun'))

class TrieNOdes:
    def __init__(self) -> None:
        self.children={}
        self.isEnd=False

class TRIE:
    def __init__(self) -> None:
        self.root=TrieNOdes()

    def add(self,word):
        curr=self.root
        for char in word:
            if char not in curr.children:
                curr.children[char]=TrieNOdes()
            curr=curr.children[char]
        curr.isEnd=True
        


class TN:
    def __init__(self) -> None:
        self.children={}
        self.isEnd=False

class TR:
    def __init__(self) -> None:
        self.root=TN()

    def add(self,word):
        curr=self.root
        for char in word:
            if char  not in curr.children:
                curr.children[char]=TN()
            curr=curr.children[char]
        curr.isEnd=True

    def search(self,word):
        curr=self.root
        for char in word:
            if char not in curr.children:
                return False
            curr=curr.children[char]
        if curr.isEnd:
            return True
        return False
    
    def removeWord(self,word):
        if not self.search(word):
            return 
        curr=self.root
        stack=[]
        for char in word:
            stack.append(char)
            curr=curr.children[char]
        curr.isEnd=False

        while stack:
            curr=stack.pop()
            char=word[len(stack)]

            if not curr.children[char].isEnd and not curr.children[char].children:
                del curr.children[char]
            else:
                break

        