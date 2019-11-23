# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        cur = head
        while cur :
            cur = cur.next
            length +=1
        length = length - n 
        cur = dummy
        while length > 0:
            cur = cur.next
            length -= 1
        cur.next = cur.next.next
        return dummy.next
