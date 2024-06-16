class Node:
    def __init__(self, data=None, next=None, prev=None):  # O(1)
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):  # O(1)
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):  # O(1)
        if self.head is None:
            self.head = self.tail = Node(data)
            return

        node = Node(data, self.head, None)
        self.head.prev = node
        self.head = node

    def insert_at_end(self, data):  # O(1)
        if self.tail is None:
            self.tail = self.head = Node(data)
            return

        node = Node(data, None, self.tail)
        self.tail.next = node
        self.tail = node

    def insert_values(self, data_array):  # O(n)
        self.head = None
        for data in data_array:
            self.insert_at_end(data)

    def insert_at(self, index, data):  # O(n)
        length = self.get_length()
        if index < 0:
            index = length + index

        if not isinstance(index, int):
            raise TypeError("List index must be integer")
        if index >= length:
            raise IndexError("List index out of range")

        if index == 0:
            self.insert_at_beginning(data)
            return
        if index == length - 1:
            self.insert_at_end(data)
            return

        mid = length // 2
        if index <= mid:
            itr = self.head
            count = 1
            while count < index:
                itr = itr.next
                count += 1
            node = Node(data, itr.next, itr)
            itr.next.prev = node
            itr.next = node
        else:
            index = index - length
            itr = self.tail
            count = -2
            while count > index:
                itr = itr.prev
                count -= 1
            node = Node(data, itr, itr.prev)
            itr.prev.next = node
            itr.prev = node

    def insert_after_value(self, data_after, data_to_insert):  # O(n)
        itr = self.head

        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next, itr)
                if itr.next is None:
                    self.insert_at_end(data_to_insert)
                    return
                itr.next.prev = node
                itr.next = node
                return
            itr = itr.next

        raise Exception(f"Value [{data_after}] was not found")

    def remove_at_beginning(self):  # O(1)
        self.head = self.head.next
        self.head.prev = None

    def remove_at_end(self):  # O(1)
        self.tail = self.tail.prev
        self.tail.next = None

    def remove_at(self, index):  # O(n)
        length = self.get_length()
        if index < 0:
            index = length + index

        if not isinstance(index, int):
            raise Exception(f"List index [{index}] must be integer")
        if index >= length:
            raise Exception(f"List index [{index}] out of range")

        if index == 0:
            self.remove_at_beginning()
            return
        if index == length - 1:
            self.remove_at_end()
            return

        mid = length // 2
        if index <= mid:
            itr = self.head
            count = 0
            while count < index - 1:
                itr = itr.next
                count += 1
            itr.next = itr.next.next
            itr.next.prev = itr
        else:
            index = index - length
            itr = self.tail
            count = -1
            while count > index + 1:
                itr = itr.prev
                count -= 1
            itr.prev = itr.prev.prev
            itr.prev.next = itr

    def remove_by_value(self, data_to_remove):  # O(n)
        if self.head.data == data_to_remove:
            self.remove_at_beginning()
            return
        itr = self.head

        while itr.next:
            if itr.data == data_to_remove:
                itr.next.prev = itr.prev
                itr.prev.next = itr.next
                itr = None
                return
            itr = itr.next

        if self.tail.data == data_to_remove:
            self.remove_at_end()
            return

        raise Exception(f"Value [{data_to_remove}] was not found")

    def print_forward(self):  # O(n)
        if self.head is None:
            print("[]")

        itr = self.head
        result_str = ""
        while itr:
            result_str += f"[{itr.data}]-->"
            itr = itr.next
        print(result_str)

    def print_backward(self):  # O(n)
        if self.tail is None:
            print("[]")

        itr = self.tail
        result_str = ""
        while itr:
            result_str += f"<--[{itr.data}]"
            itr = itr.prev
        print(result_str)

    def get_length(self):  # O(n)
        count = 0
        itr = self.head

        while itr:
            itr = itr.next
            count += 1

        return count
