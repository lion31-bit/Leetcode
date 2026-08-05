# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        temp=head
        count=0
        prev=None
        while temp.next is not None:
            count+=1
            temp=temp.next
        if n == count+1:
            new=head.next
            return new
        temp=head
        length=count-n
        pos=0
        while pos<length:
            temp=temp.next
            pos+=1
        temp.next=temp.next.next
        return head
           
        

           

            
        
     
        