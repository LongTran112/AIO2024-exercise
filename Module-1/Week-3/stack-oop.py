from typing import List

class Stack:
    def __init__(self, capacity) -> None:
        self.__capacity = capacity
        self.__items = []

    def get_items(self):
        return self.__items

    def is_empty(self):
        return True if len(self.__items) == 0 else False
    
    def is_full(self):
        return True if len(self.__items) == self.__capacity else False
    
    def pop(self):
        self.__items.remove[0]

    def push(self, value):
        if(self.is_full()):
            print("Stack is full")
            return
        self.__items.insert(0, value)
    
    def top(self):
        return self.__items[0]
    

    
stack1 = Stack(5)
stack1.push(1)
stack1.push(2)

print(stack1.top())

