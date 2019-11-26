# 循环列表 约瑟夫问题
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def create_linkList(n):
    head = Node(1)
    pre = head
    for i in range(2, n + 1):
        newNode = Node(i)
        pre.next = newNode
        pre = newNode
    pre.next = head
    return head


n = 2009  # 总的个数
m = 3  # 数的数目
# last 634
if m == 1:  # 如果是1的话，特殊处理，直接输出
    print(n)
else:
    head = create_linkList(n)
    pre = None
    cur = head
    while cur.next != cur:  # 终止条件是节点的下一个节点指向本身
        for i in range(m - 1):
            pre = cur
            cur = cur.next
        print(cur.value)
        pre.next = cur.next
        cur = cur.next
    print("final", cur.value)

