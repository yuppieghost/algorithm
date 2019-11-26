class Stack:
    def __init__(self, n):
        self.data = []
        self.max_size = n

    def init_stack(self):
        self.data = []

    def is_empty(self):
        return self.data == []

    def is_full(self):
        return len(self.data) == self.max_size

    def push(self, x):
        if self.is_full():
            raise IndexError("stack is full")
        else:
            self.data.append(x)

    def pop(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        else:
            return self.data.pop()

    def stack_top(self):
        if self.is_empty():
            print("stack is empty")
        else:
            return self.data[-1]


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkStack:
    def __init__(self):
        self.top = None

    def top(self):
        if self.top is None:
            print("stack empty")
        else:
            return self.top.val

    def push(self, x):
        tmp = self.top
        self.top = ListNode(x)
        self.top.next = tmp

    def pop(self):
        if self.top is None:
            print("stack empty")
        else:
            tmp = self.top
            self.top = self.top.next
            return tmp.val

