class MyDeque:
    def __init__(self):
        self._items = []
    
    def __len__(self):
        return len(self._items)
    
    def __str__(self):
        return f"Deque({self._items})"
    
    def append(self, x):
        self._items.append(x)
    
    def appendleft(self, x):       #ставит эл-т на поределенную позицию в спискке
        self._items.insert(0, x)
    
    def pop(self):
        return self._items.pop()
    
    def popleft(self):
        return self._items.pop(0)


deq = MyDeque()
deq.append(1)
deq.appendleft(2)
print(deq)
elt = deq.pop()
print(deq, elt)