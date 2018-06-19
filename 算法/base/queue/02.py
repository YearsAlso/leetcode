class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    node = head
    length = 0
    i = 0
    while True:
        node = node.next
        if node.next == None:
            break
        length += 1
    length -= n
    node = head
    while i < length:
        node = node.next
        i += 1

    node2 = node.next
    node.next = node2
    return node