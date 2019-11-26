class CircularQueue:
    def __init__(self, n):
        # size = n
        self.head = 0
        self.tail = 0
        self.size = n
        self.data = [None for _ in range(self.size)]

    # full condition: (tail + 1) % size == head
    # so tail pointer always point to None
    def enqueue(self, x):
        if (self.tail + 1) % self.size == self.head:
            print("full")
            return False
        self.data[self.tail] = x
        self.tail = (self.tail + 1) % self.size
        return True

    # empty condition: head == tail
    def dequeue(self):
        if self.head == self.tail:
            print('empty')
            return False
        ret = self.data[self.head]
        self.head = (self.head + 1) % self.size
        return ret

    def show(self):
        print("================================================================================")
        print(f"head,{self.head}")
        print(f"tail,{self.tail}")
        print(f"data,{self.data}")

q = CircularQueue(5)
q.show()
q.enqueue(1)
q.show()
q.enqueue(2)
q.show()
q.enqueue(3)
q.show()
