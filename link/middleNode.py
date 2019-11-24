# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        l = []
        cur = head
        while cur:
            l.append(cur)
            cur = cur.next
        return l[int(len(l)/2)]