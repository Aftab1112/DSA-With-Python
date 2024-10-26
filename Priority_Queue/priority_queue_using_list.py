class Priority_Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, data, priority):
        index = 0
        while index < len(self.items) and self.items[index][1] <= priority:
            index += 1
        self.items.insert(index, (data, priority))

    def pop(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        return self.items.pop(0)[0]

    def size(self):
        return len(self.items)


p = Priority_Queue()
p.push("China", 8)
p.push("Germany", 6)
p.push("America", 7)
p.push("Japan", 2)
p.push("Soveit Union", 3)

while not p.is_empty():
    print(p.pop())
