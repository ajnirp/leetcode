# https://leetcode.com/problems/print-immutable-linked-list-in-reverse/

# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        if head is None:
            return
        
        s = []
        while head is not None:
            s.append(head)
            head = head.getNext()
            
        while len(s) > 0:
            s.pop().printValue()