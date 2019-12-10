class DbListNode:
    def __init__(self, x, y):
        self.key = x
        self.val = y
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.hkeys = {}
        self.top = DbListNode(None, -1)
        self.tail = DbListNode(None, -1)
        self.tail.prev = self.top
        self.top.next = self.tail

    def get(self, key):
        if key in self.hkeys.keys():
            cur = self.hkeys[key]
            cur.prev.next = cur.next
            cur.next.prev = cur.prev

            top_node = self.top.next
            self.top.next = cur
            cur.next = top_node
            cur.prev = self.top
            top_node.prev = cur

            return self.hkeys[key].val
        return -1

    def put(self, key, value):
        if key in self.hkeys.keys():
            cur = self.hkeys[key]
            cur.val = value
            cur.prev.next = cur.next
            cur.next.prev = cur.prev

            top_node = self.top.next
            top_node.prev = cur
            self.top.next = cur
            cur.next = top_node
            cur.prev = self.top
        else:
            cur = DbListNode(key, value)
            self.hkeys[key] = cur
            top_node = self.top.next
            top_node.prev = cur
            self.top.next = cur
            cur.next = top_node
            cur.prev = self.top

            if len(self.hkeys.keys()) > self.cap:
                tail_node = self.tail.prev
                tail_node.prev.next = self.tail
                self.tail.prev = tail_node.prev
                self.hkeys.pop(tail_node.key)

    def __repr__(self):
        vals = []
        p = self.top.next
        while p.next:
            vals.append(str(p.val))
            p = p.next
        return '->'.join(vals)


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache)
    cache.get(1)  # 返回  1
    cache.put(3, 3)  # 该操作会使得密钥 2 作废
    print(cache)
    cache.get(2)  # 返回 -1 (未找到)
    cache.put(4, 4)  # 该操作会使得密钥 1 作废
    print(cache)
    cache.get(1)  # 返回 -1 (未找到)
    cache.get(3)  # 返回  3
    print(cache)
    cache.get(4)  # 返回  4
    print(cache)
