class Node:
    def __init__(self, item=None, priority=None, next=None):
        self.item = item
        self.priority = priority
        self.next = next


class Priority_Queue:
    def __init__(self):
        self.start = None
        self.item_count = 0

    def is_empty(self):
        return self.start == None

    def push(self, data, priority):
        n = Node(data, priority)
        if self.is_empty() or priority < self.start.priority:
            n.next = self.start
            self.start = n
        else:
            temp = self.start
            while temp.next is not None and temp.next.priority <= priority:
                temp = temp.next
            n.next = temp.next
            temp.next = n
        self.item_count += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty")
        data = self.start.item
        self.start = self.start.next
        self.item_count -= 1
        return data

    def size(self):
        return self.item_count


p = Priority_Queue()
p.push("China", 8)
p.push("Germany", 6)
p.push("America", 7)
p.push("Japan", 2)
p.push("Soveit Union", 3)

while not p.is_empty():
    print(p.pop())
