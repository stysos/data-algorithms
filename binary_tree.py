

class Node:
    
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        
    def printtree(self):
        print(self.data)
        
        
        
        
class Tree:
    
    def __init__(self, root) -> None:
        self.root = root
        
    def getroot(self):
        return self.head
    
    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(value, self.root)
            
    def _add(self, value, node):
        if value < node.value:
            if node.left is not None:
                self._add(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right is not None:
                self._add(value, node.right)
            else:
                node.right = Node(value)
    
    def printtree(self):
        if self.root is not None:
            self._printtree(self.root)
        
    def _printtree(self, node):
        if node is not None:
            self._printtree(node.left)
            print(str(node.value) + ' ')
            self._printtree(node.right) 
        

root_node = Node(15)
tree = Tree(root_node)

tree.add(50)

tree.printtree()




        