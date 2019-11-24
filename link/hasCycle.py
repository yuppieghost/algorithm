# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# s1, hashtable
# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         s = Set()
#         while head:
#             if head in s:
#                 return True
#             s.add(head)
#             head = head.next
#         return False
        

# s2 slow & fast
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next
        while (slow != fast):
            if (fast.nest is None or fast.next.next is None):
                return False
            slow = slow.next
            fast = fast.next.next
        return True