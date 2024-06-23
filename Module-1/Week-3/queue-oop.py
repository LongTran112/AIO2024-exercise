class Queue:
    def __init__(self, capacity) -> None:
        self.__capacity = capacity
        self.__items = []

    def get_items(self):
        return self.__items

    def is_empty(self):
        return True if len(self.__items) == 0 else False
    
    def is_full(self):
        return True if len(self.__items) == self.__capacity else False
    
    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty cannot dequeue")
            return 
        return self.__items.pop()

    def enqueue(self, value):
        if(self.is_full()):
            print("Queue is full")
            return
        self.__items.append(value)
    
    def front(self):
        return self.__items[0]
    
queue1 = Queue(5)

queue1.enqueue(1)
queue1.enqueue(2)

[print(item) for item in queue1.get_items()]

print(queue1.is_full())
print(queue1.dequeue())
print(queue1.front())
print(queue1.dequeue())
print(queue1.is_empty())

    
