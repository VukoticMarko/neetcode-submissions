# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        # Traverse every linked list
        for lst in lists:
            while lst: # Traverse current linked list node by node
                nodes.append(lst.val) # Save value
                lst = lst.next
        nodes.sort()

        res = ListNode(0)
        cur = res

        # Go through sorted values and make new dummy linked-list and fill it
        for node in nodes:
            cur.next = ListNode(node)
            cur = cur.next
        return res.next
        