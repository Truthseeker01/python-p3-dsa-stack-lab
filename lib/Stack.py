class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        if self.items == []:
            return True
        return False

    def push(self, item):
        if len(self.items) < self.limit:
            return self.items.append(item)
        return None

    def pop(self):
        if self.items == []:
            return None
        return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        if len(self.items) != 0:
            return True
        return False

    def search(self, target):
        if target in self.items:
            return self.items.index(self.items[-1]) - self.items.index(target)
        return -1
