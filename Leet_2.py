# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        cur = dummy 
        total = 0
        carry = 0
        while l1 is not None or l2 is not None or carry != 0 :

            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0


            total = v1 + v2 + carry 
            digit = total % 10
            carry = total // 10 

            cur.next = ListNode(digit)
            cur = cur.next 

            if l1 : l1 = l1.next 
            if l2 : l2 = l2.next 

        return dummy.next