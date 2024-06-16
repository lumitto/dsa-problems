from dsa_utils.linked_list import create_ll, print_ll, ListNode
from typing import Optional

# My Solution
class Solution:
    def getLength(self, head: Optional[ListNode]) -> int:
        """Time Complexity O(n); Auxiliary Space Complexity - O(1)"""
        itr = head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Time Complexity O(n); Auxiliary Space Complexity - O(1)"""
        length = self.getLength(head)
        itr = head
        current = 0
        mid = length // 2
        while current < mid:  # Stops when necessary node is reached
            current += 1
            itr = itr.next
        return itr


# Two Pointers solution. Idea taken from DevOgabek
# [https://leetcode.com/problems/middle-of-the-linked-list/solutions/4834682/beat-100-00-full-explanation-with-pictures/]
# class Solution:
#     def middleNode(self, head: ListNode) -> ListNode:
#         """Time Complexity O(n); Auxiliary Space Complexity - O(1)"""
#         slow_pointer = head
#         fast_pointer = head
#
#         while fast_pointer is not None and fast_pointer.next is not None:
#             slow_pointer = slow_pointer.next
#             fast_pointer = fast_pointer.next.next
#         return slow_pointer


# Test
ll = create_ll([1, 2, 3, 4, 5])
print_ll(ll)

solution = Solution()
mid_node = solution.middleNode(ll)
print_ll(mid_node)
