from singly_linked_list import *


class Stack:
    def __init__(self):
        self.my_list = SLL()
        self.item_count = 0

    def is_empty(self):
        return self.my_list.is_empty()

    def push(self, data):
        self.my_list.insert_at_start(data)
        self.item_count += 1

    def pop(self):
        if not self.is_empty():
            self.my_list.delete_first()
            self.item_count -= 1

    def peek(self):
        if not self.is_empty():
            return self.my_list.start.item

    def size(self):
        return self.item_count


s = Stack()
s.push(10)
s.push(20)
s.push(30)
print("Top element is : ", s.peek())
s.pop()
print("Top element is : ", s.peek())
