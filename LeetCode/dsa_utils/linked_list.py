class ListNode:
    """Definition of Singly-Linked List Node taken from Leet Code"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_ll(array) -> ListNode:
    """Time complexity - O(n);
    Auxiliary Space Complexity - O()"""
    head = ListNode(array[0])
    i = head
    for val in array[1:]:
        i.next = ListNode(val)
        i = i.next
    return head


def print_ll(head: ListNode):
    """Time complexity - O(n)"""
    result = ""
    itr = head
    while itr:
        result += str(itr.val) + "-->"
        itr = itr.next
    print(result)
