from dsa_utils.linked_list import create_ll, print_ll


# Definition for singly-linked list.
class ListNode:
    """Time Complexity O(1); Auxiliary Space Complexity - O(1)"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getLength(self, head: ListNode) -> int:
        """Time Complexity O(n); Auxiliary Space Complexity - O(1)"""
        itr = head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def middleNode(self, head: ListNode) -> ListNode:
        """Time Complexity O(n); Auxiliary Space Complexity - O(1)"""
        length = self.getLength(head)
        itr = head
        current = 0
        mid = length // 2
        while current < mid:  # Stops when necessary node is reached
            current += 1
            itr = itr.next
        return itr


# Test
ll = create_ll([1, 2, 3, 4, 5])
print_ll(ll)

solution = Solution()
mid_node = solution.middleNode(ll)
print_ll(mid_node)
