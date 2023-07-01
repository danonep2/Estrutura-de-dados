class No:
    def __init__(self, value):
        self.value = value
        self.next = None

class LiscaCircular:
    def __init__(self):
        self.start = None
        self.end = None
        self.len = 0
    
    def add(self, value):
        new = No(value)
        self.len += 1
        if self.start is None:
            new.next   = new
            self.start = new
            self.end   = new
            return

        self.end.next = new
        self.end = new
        self.end.next = self.start
    
    def __str__(self):
        if self.len == 0:
            return "[]"
        
        res = "["
        pointer = self.start
        while pointer.next.next != self.start.next:
            res = res + str(pointer.value) + ","
            pointer = pointer.next

        return res[:-1] + "]"
    
    def __len__(self):
        return self.len
    
    def pop(self):
        if self.len == 0: return
        if self.len == 1:
            self.start = None
            self.end = None
            self.len = 0
            return
        
        self.len -= 1

        pointer = self.start
        while pointer:
            if pointer.next == self.end:
                pointer.next = self.start
                return 
            pointer = pointer.next
    
    def get(self, index):
        if index > self.len: return

        pointer = self.start
        for i in range(index):
            pointer = pointer.next
        
        return "[" + str(pointer.value) + "]"
    
    def remove(self, value):
        if self.start.value == value:
            self.start = self.start.next
            self.end.next = self.start
            return

        pointer = self.start
        while pointer.next.next != self.start.next:
            if pointer.next.value == value:
                pointer.next = pointer.next.next
                return

            pointer = pointer.next
        
