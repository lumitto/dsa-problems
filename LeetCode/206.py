from dsa_utils.linked_list import create_ll, print_ll, ListNode
from typing import Optional


# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         """Time Complexity - O(n); Auxiliary Space Complexity - O(n)"""
#         if head is None:
#             return None
#         itr = head
#         array = []
#         while itr:
#             array.append(itr.val)
#             itr = itr.next
#
#         array = array[::-1]
#
#         head = ListNode(array[0])
#         itr = head
#         for node in array[1:]:
#             itr.next = ListNode(node)
#             itr = itr.next
#         return head


# Inspired by niits solution
# [https://leetcode.com/problems/reverse-linked-list/solutions/5152548/video-solution-with-visualization/]
# When I started to read an explanation I got an idea of three variables: prev, head and temp that allows
# proper link exchange. So I tried to implement the solution by myself before I continue to read niits's one.
# Here is a result. It's obviously better than my previous solution as it iterates through the list only once and takes
# less space. I think it is sill not the best implementation, but I'm proud of myself :)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Time Complexity - O(n); Auxiliary Space Complexity - O(1)"""
        if head is None:
            return None
        prev = None
        head = head
        temp = head.next
        while head.next:
            head.next = prev
            prev = head
            head = temp
            temp = head.next
        head.next = prev
        prev = head
        return prev


# Test
ll = create_ll(list(range(1, 20)))
print_ll(ll)

solution = Solution()
print_ll(solution.reverseList(ll))

