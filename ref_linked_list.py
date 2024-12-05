class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def from_list(values):
        """Construct a linked list from a list of values."""
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

    def print(self):
        """Print the linked list in a readable format."""
        current = self
        elements = []
        while current:
            elements.append(str(current.val))
            current = current.next
        print(" -> ".join(elements))

    @staticmethod
    def are_equal(list1, list2):
        """Check if two linked lists are equal."""
        current1, current2 = list1, list2
        while current1 and current2:
            if current1.val != current2.val:
                return False
            current1 = current1.next
            current2 = current2.next
        return current1 is None and current2 is None

    def to_list(self):
        """Convert the linked list to a Python list."""
        current = self
        result = []
        while current:
            result.append(current.val)
            current = current.next
        return result


def reverse_list(head: ListNode) -> ListNode:
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev, cur = cur, nxt
    return prev


def list_length(head: ListNode) -> int:
    length = 0
    cur = head
    while cur:
        length += 1
        cur = cur.next
    return length


def test():
    import numpy as np

    def rand_list():
        return list(np.random.randint(0, 100, size=np.random.randint(0, 10)))

    for _ in range(3):
        l = rand_list()
        original_list = ListNode.from_list(l)

        # Test reverse_list
        reversed_list = reverse_list(original_list)
        assert ListNode.are_equal(reversed_list, ListNode.from_list(l[::-1]))
        print("ok")

        # Test list_length
        assert list_length(ListNode.from_list(l)) == len(l)
        print("ok")


test()
