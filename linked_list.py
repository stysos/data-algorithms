class Node:
    
    def __init__(self, dataval):
        self.dataval = dataval
        self.nextval = None
        
    def __str__(self):
        return self.dataval
    
    def __next__(self):
        return self.nextval.dataval

class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
            
    def insert_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.nextval = self.head
        self.head = new_node
        

linked = LinkedList()
linked.head = Node('Monday')
n2 = Node('Tuesday')
n3 = Node('Wednesday')
linked.head.nextval = n2

n2.nextval = n3

linked.listprint()

linked.insert_beginning('Sunday')
linked.listprint()

