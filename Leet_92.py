class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0 , head)
        leftPrev = dummy 

        cur = head

        for _ in range(left - 1) :
            leftPrev  , cur =  cur , cur.next

        prev = None
        for _ in range(right - left + 1) :
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        leftPrev.next.next = cur
        leftPrev.next = prev

        return dummy.next      
        
