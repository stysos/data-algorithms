class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.value})"

    def printtree(self):
        print(self.data)


class Tree:
    def __init__(self, root) -> None:
        self.root = root

    def getroot(self):
        return self.root
    
    def delete(self, value):
        if self.root is None:
            return
        
        self._delete(value, self.root)
        
    def _find_lowest_right(self, node):
        if node.right:
            self._find_lowest_right(node.right)
        
    def _delete(self, value, node):
        #TODO: Implement iterative
        """
        
        if value == node.value:
            #TODO: Get largest smallest left
            if node.left:
                self.find_lowest_right(node.left)
            else:
                #TODO: No left node event
                    if node.right:
                        right = node.right
                    set parent to node
                    parent.right = right
                    
        
        if value < node.value:
            self._delete(value, node.left)
            
        elif node.right == val
            
        else:
            node.right is not None:
            self._delete(value, node.right)
        
        if 
        
        """

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

    def walk(self, path):
        if self.root is None:
            return path
        else:
            self._walk(self.root, path)

    def _walk(self, curr, path) -> None:
        if curr is None:
            return

        self._walk(curr.left, path)
        path.append(curr.value)
        self._walk(curr.right, path)

    def printtree(self):
        if self.root is None:
            return
        self._printtree(self.root)

    def _printtree(self, node):
        if node is None:
            return
        self._printtree(node.left)
        print(str(node.value) + " ")
        self._printtree(node.right)


root_node = Node(15)
root_node.left = Node(1)
root_node.right = Node(6)
tree = Tree(root_node)

tree.add(50)
path = []
tree.walk(path)
print(path)
