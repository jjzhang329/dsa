# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.

# Approach: using two pointers slow and fast. fast will be movin n steps faster
# so when fast is at the end, we know the next on slow is pointing need to be deleted.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        slow = dummy
        fast = dummy 
        for i in range(n+1):
            fast = fast.next
        
        while fast:
            slow = slow.next 
            fast = fast.next 
        slow.next = slow.next.next
        
        return dummy.next

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]