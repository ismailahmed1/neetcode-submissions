# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1 -> None,  2 -> 3 -> 4 -> 5
        # prev = 1
        #curr = 2
       
        prev = None
        curr = head

        while curr:
            next_node = curr.next #2
            curr.next = prev #1 -> None
            prev = curr #prev = 1 
            curr = next_node #curr = 2 
        
        return prev