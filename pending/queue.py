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


# e.g
# q = CircularQueue(5)
# q.show()
# q.enqueue(1)
# q.show()
# q.enqueue(2)
# q.show()
# q.enqueue(3)
# q.show()
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkQueue:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None and self.rear is None

    def dequeue(self):
        if self.is_empty():
            return False
        tmp = self.front
        self.front = tmp.next
        return tmp.val

    def enqueue(self, x):
        node = Node(x)
        if self.is_empty():
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
