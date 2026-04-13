class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.append(data)   # add at the back

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)  # remove from front (slow, but simple)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def front(self):
        if self.is_empty():
            return None
        return self.items[0]

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())  # 10
print(q.dequeue())  # 20
print(q.front())    # 30