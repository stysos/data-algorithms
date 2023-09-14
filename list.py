class CustomList:
    
    def __init__(self) -> None:
        self.items = []
        self.count = 0
        
    def append(self, item):
        self.items += [item]
        self.count += 1
        
    def __len__(self):
        return self.count
    
    def __getitem__(self, index):
        if index < 0 or index >= self.count:
            raise IndexError('CustomList index out of range')
        return self.items[index]
    
    def __delitem__(self, index):
        if index < 0 or index >= self.count:
            raise IndexError('CustomList index out of range')
        self.items = self.items[:index] + self.items[index+1:]
        self.count -= 1
        
    def __str__(self):
        return '[' + ', '.join(str(item) for item in self.items) + ']'
    
    def __repr__(self):
        return str(self)

    def insert(self, index, item):
        if index < 0 or index > self.count:
            raise IndexError('CustomList index out of range')
        self.items = self.items[:index] + [item] + self.items[index:]
        self.count += 1

    def remove(self, item):
        if item not in self.items:
            raise ValueError(f"{item} not in CustomList")
        for i in range(self.count):
            if self.items[i] == item:
                del self[i]
                break

    def pop(self, index=None):
        if index is None:
            index = self.count - 1
        if index < 0 or index >= self.count:
            raise IndexError('CustomList index out of range')
        item = self.items[index]
        del self[index]
        return item

    def clear(self):
        self.items = []
        self.count = 0

# Testing the CustomList
cl = CustomList()
cl.append(5)
cl.append(10)
print(cl)  # [5, 10]
print(len(cl))  # 2
print(cl[1])  # 10

cl.insert(1, 7)
print(cl)  # [5, 7, 10]

cl.remove(7)
print(cl)  # [5, 10]

print(cl.pop())  # 10
print(cl)  # [5]




    