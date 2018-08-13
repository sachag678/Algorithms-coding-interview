"""Linked list."""


class Node():
    """Singly linked list."""

    def __init__(self, data):
        """Setup the node."""
        self.next = None
        self.data = data

    def __repr__(self):
        """Show list."""
        s = ''
        n = self
        while n.next is not None:
            s += str(n.data)
            if n.next is not None:
                s += '-->'
            n = n.next

        s += str(n.data)
        return s

    def append_to_tail(self, data):
        """Read through the list and add the data node to the end of the list."""
        end = Node(data)
        n = self
        while n.next is not None:
            n = n.next

        n.next = end

    def delete_node(self, head, data):
        """Delete node."""
        n = head

        if n.data == data:
            return head.next

        while n.next is not None:
            if n.next.data == data:
                n.next = n.next.next
                return head
            n = n.next

        return head


def remove_dups(linked_list):
    """Remove duplicates from the singly linked list. Chapter 2, problem 2.1."""
    buffer = []
    n = linked_list
    while n.next is not None:
        if buffer.__contains__(n.next.data):
            n.next = n.next.next
        else:
            buffer.append(n.data)
        n = n.next
        if n is None:
            break
    return linked_list


def kth_to_last(linked_list, k, index=[0]):
    """Find the kth to last element. i.e., if k=1 return the last element, if k=2 return the second to last element.

    The assumption is that the length of the list is unknown.
    """
    if linked_list is None:
        return None
    
    node = kth_to_last(linked_list.next, k, index)
    index[0] += 1 
    if index[0] == k:
        return linked_list

    return node
    
def test():
    linked_list = Node(1)
    for i in range(5):
        linked_list.append_to_tail(i)

    linked_list.append_to_tail(1)

    print(linked_list)
    print(remove_dups(linked_list))

if __name__ == '__main__':
    linked_list = Node(1)
    linked_list.append_to_tail(2)
    linked_list.append_to_tail(3)

    print(kth_to_last(linked_list, 2))
    
