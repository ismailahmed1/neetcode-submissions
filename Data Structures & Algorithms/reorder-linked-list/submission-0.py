# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        linked_map = {}
        index = 0 
        curr = head
        while curr != None:
            linked_map[index] = curr
            index += 1
            curr = curr.next

        n = index
        
        l = 0 
        r = index - 1
        for i in range (n - 1):
            if i % 2 == 0:
                linked_map[l].next = linked_map[r]
                l += 1
            else:
                linked_map[r].next = linked_map[l]
                r -=1 
        
        linked_map[l].next = None
        


        
    