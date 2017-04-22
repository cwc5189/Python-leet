# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        primary = l1
        secondary = l2
        start = ListNode(0)
        
        while(primary.next is not None and secondary.next is not None):
            primary = primary.next;
            secondary = secondary.next;
        
        if primary.next is not None:
            primary = l1
            secondary = l2
        else:
            primary = l2
            secondary = l1
        
        cur = start
        curP = primary
        curS = secondary
        
        while curP is not None:
            sValue = 0
            if curS is not None:
                sValue = curS.val
            
            sum = curP.val + sValue
            
            cur.next = ListNode(sum%10)
            
            if sum >= 10:
                if curP.next is None:
                    curP.next = ListNode(1)
                else:
                    curP.next.val = curP.next.val + 1
            
            cur = cur.next
            curP = curP.next
            if curS is not None:
                curS = curS.next
        
        return start.next