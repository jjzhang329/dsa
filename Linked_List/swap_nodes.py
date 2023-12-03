# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        current = dummy_head
        
        while current.next and current.next.next:
            next1 = current.next #original node(1)
            next2 = current.next.next.next #original node(3)
            current.next = next1.next #dummy -> node(2)
            current.next.next = next1  #node(2) -> node(1)
            next1.next = next2 #original node(1) -> node(3)
            current = current.next.next #move current pointer to node (3)
        
        return dummy_head.next

# Input: head = [1,2,3,4]
# Output: [2,1,4,3]