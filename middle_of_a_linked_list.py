# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        q=deque([])
        curr=head
        while curr:
            q.append(curr)
            curr=curr.next
        
        n=math.ceil(len(q)/2)-1
        while n>0:
            q.pop()
            n-=1
        return q[-1]