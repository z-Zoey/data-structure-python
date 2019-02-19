# Singly linked list implemenation(O(1) insertions and deletions, O(n) for access)
class Node(object):

    def __init__(self, val):

        self.val = val
        self.next = None


# Doubly linked list implementation
class DoubleNode(object):

    def __init__(self, val):

        self.val = val
        self.next = None
        self.prev = None


# Returns a boolean if the singly linked list contains a loop
def cycle_check(node):
    marker1 = node
    marker2 = node

    while marker2 != None and marker2.next != None:

        marker1 = marker1.next
        marker2 = marker2.next.next

        if marker2 == marker1:
            return True

    return False
