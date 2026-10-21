# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        linked_map = {}
        length = 0
        curr = head

        while curr != None:
            linked_map[length] = curr
            length += 1
            curr = curr.next


        if n == length:
            return head.next
        
        if n == 1:
            linked_map[length - n - 1].next = None
        else:
            linked_map[length - n - 1].next = linked_map[length - n + 1]

        return head
        

            