# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Prepend a temporary head so we can return an empty set if need be
        newHead = ListNode(0)
        newHead.next = head
        
        # Create two pointers, one to current value and one for the lookahead
        track = newHead
        lookahead = newHead

        # Set lookahead ahead by n, so this will hit the end of the list when we hit
        # the element we need to remove. (Also account for our prepended head!)
        for i in range(n+1):
            lookahead = lookahead.next
        
        # Iterate through list, incrementing both pointers
        # When the lookahead hits the end of the list, set current node's
        # next to the second next element
        while track is not None:
            if lookahead is None:
                lookahead = track
                track.next = track.next.next
            
            track = track.next
            lookahead = lookahead.next
        
        return newHead.next