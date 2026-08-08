# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head

        prev = head
        temp = head.next

        while temp is not None:
            if temp.val == prev.val:
                prev.next = temp.next
                if temp.next:
                    temp.next.prev = prev
                temp = temp.next
            else:
                prev = temp
                temp = temp.next
        return head
        
        