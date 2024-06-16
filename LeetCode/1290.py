class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        itr = head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        power = count - 1
        result = 0
        while itr:
            result += itr.val * 2 ** power
            power -= 1
            itr = itr.next
        return result
