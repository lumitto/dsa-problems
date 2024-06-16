from dsa_utils.linked_list import create_ll, print_ll, ListNode
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Time Complexity - O(n); Auxiliary Space Complexity - O(n)"""
        if head is None:
            return None
        itr = head
        array = []
        while itr:
            array.append(itr.val)
            itr = itr.next

        array = array[::-1]

        head = ListNode(array[0])
        itr = head
        for node in array[1:]:
            itr.next = ListNode(node)
            itr = itr.next
        return head


ll = create_ll([1, 2, 3, 4, 5])
print_ll(ll)

solution = Solution()
print_ll(solution.reverseList(ll))

